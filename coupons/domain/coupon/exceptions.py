class CouponAlreadyRegisteredError(Exception):
    def __init__(
        self,
        code: str,
        message="Coupon alredy registered for this company"
    ):
        super().__init__(message)
        self.msg = message
        self.code = code

    def as_dict(self):
        return {"message": self.msg, "code": self.code}