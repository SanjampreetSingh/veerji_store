from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_201_CREATED
)


class ResponseUtils:
    @staticmethod
    def respond_error(
        success: bool = False,
        details: str = "Business Error",
        error_message: str = None,
        status=HTTP_400_BAD_REQUEST
    ):
        """
        This is used to invoke error responses.

        Args:
            success (bool, optional): Defaults to False.
            details (str, optional): Defaults to "Business Error".
            error_message (str, optional): Defaults to None.
            status ([obj], optional): Defaults to HTTP_400_BAD_REQUEST.

        Returns:
            Dict: It is a dictionary response.s
        """
        return Response(
            {
                "success": success,
                "details": details,
                "error":
                {
                    "error_message": error_message
                }
            },
            status=status
        )

    @staticmethod
    def respond_failure(
        success=False,
        details="Invalid",
        status=HTTP_400_BAD_REQUEST
    ):
        return Response(
            {
                "success": success,
                "details": details
            },
            status=status
        )

    @staticmethod
    def respond_success(
        success=True,
        details="Success",
        status=HTTP_200_OK
    ):
        return Response(
            {
                "success": success,
                "details": details
            },
            status=status
        )

    @staticmethod
    def respond_data(
        success: bool = True,
        details: str = "Success",
        data: dict = None,
        status=HTTP_200_OK
    ):
        return Response(
            {
                "success": success,
                "details": details,
                "data": data
            },
            status=status
        )

    @staticmethod
    def respond_created(
        success=True,
        details="Success",
        status=HTTP_201_CREATED
    ):
        return Response(
            {
                "success": success,
                "details": details,
            },
            status=status
        )
