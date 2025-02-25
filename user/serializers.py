from djoser.serializers import UserCreateSerializer
from user.models import UserAccount

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = UserAccount
        fields = (
            "id",
            "email",
        )
