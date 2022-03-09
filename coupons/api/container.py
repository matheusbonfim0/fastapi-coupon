from dataclasses import dataclass
from typing import Callable, cast

from coupons.domain.coupon.protocols import CouponRepo

from coupons.infra.database.repositories.coupon_repository import CouponRepoSQLAlchemy

@dataclass(frozen=True)
class Dependencies:
    coupon_repo: CouponRepo

def _build_dependencies() -> Callable[[], Dependencies]:
    deps = Dependencies(
        coupon_repo=cast(CouponRepo, CouponRepoSQLAlchemy),
    )

    def fn() -> Dependencies:
        return deps
    
    return fn

get_dependencies = _build_dependencies()