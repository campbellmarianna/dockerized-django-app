from rest_framework import serializers
from workout.models import Rep, Set, Workout

class RepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rep
        fields = '__all__'

# One Set can have 3 reps
class SetSerializer(serializers.ModelSerializer):
    reps = RepSerializer(read_only=True, many=True)

    class Meta:
        model = Set
        fields = '__all__'

# one workout can have 3 sets
class WorkoutSerializer(serializers.ModelSerializer):
    set = SetSerializer(read_only=True, many=True)

    class Meta:
        model = Workout
        fields = '__all__'
