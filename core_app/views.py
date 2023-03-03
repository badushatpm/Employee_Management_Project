from rest_framework.response import Response
from rest_framework import status, generics
from core_app.models import Employee
from core_app.serializers import EmployeeSerializer
from datetime import datetime


class EmployeeView(generics.GenericAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get(self, request):
        search_param = request.GET.get("search")
        employees = Employee.objects.all()
        if search_param:
            employees = employees.filter(name__icontains=search_param)
        serializer = self.serializer_class(employees, many=True)
        return Response({
            "status": "success",
            "data": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailView(generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_employee(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        employee = self.get_employee(pk=pk)
        if employee is None:
            return Response({"status": "fail", "message": f"Employee with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(employee)
        return Response({"status": "success", "data": serializer.data})

    def patch(self, request, pk):
        employee = self.get_employee(pk)
        if employee is None:
            return Response({"status": "fail", "message": f"Employee with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updated_at'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_employee(pk)
        if employee is None:
            return Response({"status": "fail", "message": f"Employee with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

