from django.http import HttpResponse


from django.shortcuts import render, redirect
from .forms import TeacherForm, GroupForm
from .models import Teacher, Group


def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("teacher_list")
    else:
        form = TeacherForm()
    return render(request, "teacher_form.html", {"form": form})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teacher_list.html", {"teachers": teachers})


def add_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("group_list")
    else:
        form = GroupForm()
    return render(request, "group_form.html", {"form": form})


def group_list(request):
    groups = Group.objects.all()
    return render(request, "group_list.html", {"groups": groups})
