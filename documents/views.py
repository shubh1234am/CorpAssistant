from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.contrib.auth.views import LoginView
import os

from .forms import DocumentForm
from .models import Document, Conversation, Message
from .utils import extract_text_from_pdf
from .vectorizer import process_document
from .chroma_db import store_chunks
from .rag import ask_company
from django.contrib.auth import logout



# ==========================================================
# Upload PDF
# ==========================================================
class CustomLoginView(LoginView):
    template_name = "registration/login.html"

    def get_success_url(self):

        if self.request.user.is_staff:
            return "/admin-dashboard/"

        return "/chat/"
@login_required
def upload_document(request):

    if request.method == "POST":

        form = DocumentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            document = form.save()

            extracted_text = extract_text_from_pdf(
                document.file.path
            )

            document.content = extracted_text
            document.save()

            chunks = process_document(
                extracted_text
            )

            store_chunks(chunks)

            print("Document processed successfully.")

            # Clear the form after successful upload
            form = DocumentForm()

    else:

        form = DocumentForm()

    # Search documents
    search_query = request.GET.get(
        "search",
        ""
    )

    documents = Document.objects.all()

    if search_query:

        documents = documents.filter(
            title__icontains=search_query
        )

    documents = documents.order_by(
        "-uploaded_at"
    )

    return render(
        request,
        "documents/upload.html",
        {
            "form": form,
            "documents": documents,
            "search_query": search_query,
        }
    )
@login_required
def delete_document(request, document_id):

    document = get_object_or_404(
        Document,
        id=document_id
    )

    # Delete file from media folder
    if document.file:

        if os.path.isfile(document.file.path):

            os.remove(document.file.path)

    # Delete database record
    document.delete()

    return redirect("upload_document")    


# ==========================================================
# Main Chat
# ==========================================================

@login_required
def chat(request):

    if request.method == "POST":

        question = request.POST.get(
            "question",
            ""
        ).strip()

        conversation_id = request.POST.get(
            "conversation_id"
        )

        if conversation_id:

            conversation = Conversation.objects.get(
                id=conversation_id,
                user=request.user
            )

        else:

            conversation = Conversation.objects.create(
                user=request.user,
                title=question[:50]
            )

        Message.objects.create(
            conversation=conversation,
            sender="user",
            content=question
        )

        answer = ask_company(question)

        Message.objects.create(
            conversation=conversation,
            sender="assistant",
            content=answer
        )

        conversation.updated_at = timezone.now()
        conversation.save()

        return JsonResponse({
            "answer": answer,
            "conversation_id": conversation.id
        })

    conversations = Conversation.objects.filter(
        user=request.user
    ).order_by("-updated_at")

    return render(
        request,
        "documents/chat.html",
        {
            "conversations": conversations,
            "messages": [],
            "current_conversation": None
        }
    )


# ==========================================================
# Open Existing Conversation
# ==========================================================

@login_required
def conversation(request, conversation_id):

    conversation = get_object_or_404(
        Conversation,
        id=conversation_id,
        user=request.user
    )

    conversations = Conversation.objects.filter(
        user=request.user
    ).order_by("-updated_at")

    messages = Message.objects.filter(
        conversation=conversation
    ).order_by("created_at")

    return render(
        request,
        "documents/chat.html",
        {
            "conversations": conversations,
            "current_conversation": conversation,
            "messages": messages,
        }
    )


# ==========================================================
# Signup
# ==========================================================

def signup_view(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    else:

        form = UserCreationForm()

    return render(
        request,
        "registration/signup.html",
        {
            "form": form
        }
    )
def logout_view(request):

    print("METHOD:", request.method)

    if request.method != "GET":
        return HttpResponse(f"Request method is {request.method}")

    logout(request)

    return redirect("login")
    
@login_required
def admin_dashboard(request):

    context = {
        "document_count": Document.objects.count(),
        "conversation_count": Conversation.objects.count(),
        "recent_documents": Document.objects.order_by("-uploaded_at")[:5],
    }

    return render(
        request,
        "documents/admin_dashboard.html",
        context,
    )   