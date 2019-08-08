from rest_framework import serializers
from django.contrib.auth.models import User
from quiz.models import Advice, Quiz, QuizResults


# class UserSerializer(serializers.ModelSerializer):
#     # users = serializers.PrimaryKeyRelatedField(many=True, queryset=Quiz.objects.all())
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'user']


class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = ['id', 'title', 'content', 'tags', 'date']


# class QuizResultsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = QuizResults
#         fields = ['id', 'results', 'user', 'quiz']

# class QuizResultsSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True, many=True)
#     class Meta:
#         model = QuizResults
#         fields = '__all__'

# class QuizResultsSerializer(serializers.ModelSerializer):
#     id = serializers.ReadOnlyField(source='user.id')
#     name = serializers.ReadOnlyField(source='user.username')
#
#     class Meta:
#         model = QuizResults
#         fields = ('id', 'name', 'results', )


# class QuizSerializer(serializers.ModelSerializer):
#     # owner = UserSerializer(source='username', read_only=True)
#
#     user = UserSerializer(many=True, read_only=True)
#     quiz_to_user = QuizResultsSerializer(read_only=True)
#
#     class Meta:
#         model = Quiz
#         # fields = ['id', 'question', 'answer_1', 'answer_2', 'answer_3', 'advice', 'user', 'quiz_to_user']
#         fields = ['user', 'quiz_to_user']

# class QuizSerializer(serializers.ModelSerializer):
#     # users = QuizResultsSerializer(source='quizresults_set', many=True)
#     class Meta:
#         model = Quiz
#         fields = '__all__'


class QuizResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResults
        firlds = ['id', 'quiz', 'results']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'question', 'answer_1', 'answer_2', 'answer_3', 'advice', 'user']

        def get_users(selfself, obj):
            qset = QuizResults.objects.filter(user=obj)
            return [QuizResultsSerializer(m).data for m in qset]


# class MembershipSerializer(serializers.ModelSerializer):
#     """Used as a nested serializer by MemberSerializer"""
#     class Meta:
#         model = Membership
#         fields = ('id','group','join_date')
#
# class MemberSerializer(serializers.ModelSerializer):
#     groups = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Member
#         fields = ('id','name','groups')
#
#     def get_groups(self, obj):
#         "obj is a Member instance. Returns list of dicts"""
#         qset = Membership.objects.filter(member=obj)
#         return [MembershipSerializer(m).data for m in qset]




#
# The serializers:
#
# # serializers.py
# class PersonSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Person
#         fields = ('name',)
#
#
# class LitigantSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Litigant
#         fields = ('person', 'case', 'role')
#
#
# class CaseSerializer(serializers.ModelSerializer):
#
#     #queryset = Litigant.objects.all()
#     litigants = PersonSerializer(many=True, read_only=True)
#     case_to_person = LitigantSerializer(many=True)
#
#     class Meta:
#         model = Case
#         fields = ('summary', 'litigants', 'case_to_person')
