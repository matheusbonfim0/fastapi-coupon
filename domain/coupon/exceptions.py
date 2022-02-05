class CouponAlreadyRegisteredError(Exception):
    def __init__(
        self,
        name: str,
        message="Coupon alredy registered for this company"
    ):
        super().__init__(message)
        self.msg = message
        self.name = name

    def as_dict(self):
        return {"message": self.message, "name": self.name}