from django.shortcuts import render


def policy(request):
    template = "core/policy.html"
    return render(request, template)


def page_not_found(request, exception):
    return render(
        request,
        "core/404_page_not_found.html",
        {"path": request.path},
        status=404,
    )


def csrf_failure(request, exception):
    return render(request, "core/403_permission_denied.html", status=403)
