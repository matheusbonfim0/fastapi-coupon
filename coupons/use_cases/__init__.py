from coupons.api.container import get_dependencies

from coupons.use_cases.create_coupon_use_case import CreateCouponUseCase

coupon_repo = get_dependencies().coupon_repo
create_coupon = CreateCouponUseCase(repo=coupon_repo)