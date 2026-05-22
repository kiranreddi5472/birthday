import io
import random
from django.http import FileResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from gtts import gTTS

from .models import Wish, Gallery, Dialogue
from .serializers import WishSerializer, GallerySerializer, DialogueSerializer

class WishViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows wishes to be viewed or submitted.
    """
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    # Allow any client to list and create wishes
    http_method_names = ['get', 'post', 'delete', 'head', 'options']


class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows admin uploaded gallery memories to be viewed.
    """
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class DialogueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trainer's famous dialogues to be listed and created.
    """
    queryset = Dialogue.objects.all()
    serializer_class = DialogueSerializer
    http_method_names = ['get', 'post', 'delete', 'head', 'options']


class VoiceMessageView(APIView):
    """
    Custom endpoint that uses Google Text-to-Speech (gTTS) to generate 
    an MP3 voice greeting and streams it to the user's browser.
    """
    def get(self, request, *args, **kwargs):
        text = request.query_params.get(
            'text', 
            "Happy Birthday to our incredible trainer! Thank you for helping us debug our code, "
            "teaching us to build beautiful things, and guiding us daily. We appreciate you, Sir!"
        )
        lang = request.query_params.get('lang', 'en')
        
        try:
            # Generate the TTS audio payload
            tts = gTTS(text=text, lang=lang, slow=False)
            
            # Write to a byte buffer in memory instead of disk
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            
            # Serve as streaming audio response
            response = FileResponse(
                fp, 
                content_type='audio/mp3', 
                as_attachment=False, 
                filename='birthday_surprise.mp3'
            )
            return response
            
        except Exception as e:
            # Return descriptive error so frontend can fall back to Web Speech Synthesis API
            return Response(
                {
                    "error": "Failed to compile text-to-speech online. Using client synthesis fallback.",
                    "details": str(e)
                }, 
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )


# List of premium, fun, trainer-centric random wishes
RANDOM_MESSAGES = [
    "Wishing the absolute best mentor a fantastic birthday! Thanks for always keeping our code running and our spirits high! 💻✨",
    "Happy Birthday Sir! Your passion for teaching is as infinite as an accidental while loop! 🚀",
    "To the trainer who taught us that debugging is just detective work: Have an amazing birthday! 🕵️‍♂️🎉",
    "May your birthday be free of syntax errors and filled with joy! You are the best coach ever! 🎂🔥",
    "Practice makes a man perfect, and your training made us developers! Happy Birthday, Coach! 💯",
    "Happy Birthday, Sir! You make complex algorithms look like child's play. Thanks for being awesome! 🌟",
    "Happy Birthday, Sensei! You didn't just teach us language syntaxes; you taught us how to think! 🧠🏆"
]

@api_view(['GET'])
def random_message(request):
    """
    Returns a random heartwarming birthday wish for the trainer.
    """
    msg = random.choice(RANDOM_MESSAGES)
    return Response({"message": msg})
