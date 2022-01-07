"""
All Data Base Schema will be mapped under this file.
"""
from pydantic.datetime_parse import datetime
from typing import List, Optional
from pydantic import BaseModel


class Assessment(BaseModel):
    slug: str
    total_candidates: int

    class Config:
        orm_mode = True


class AssessmentCreate(Assessment):
    slug: str
    total_candidates: int

    class Config:
        orm_mode = True


class SignUp(BaseModel):
    user_name: str
    password: str
    email: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    user_name: str
    password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Tenant(BaseModel):
    tenant_name: str
    status: bool
    user_id: str
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True


class SkillMaster(BaseModel):
    skill_name: str
    user_id: str
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True


class Partner(BaseModel):
    partner_name: str
    user_id: str
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True


class Application(BaseModel):
    application_name: str
    user_id: str
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True


class CategoryMaster(BaseModel):
    category_type: str
    user_id: str
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True


class AssessmentPartner(BaseModel):
    partner_name: str
    partner_type: int
    status: bool
    subscription_key: str
    subscription_password: str
    user_id: str
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True


class SubscriptionMaster(BaseModel):
    tenant_id: int
    partner_id: int
    subscription: bool
    user_id: str
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True


class AssessmentMapping(BaseModel):
    test_id: str
    application_master_id: int
    skill_master_id: int
    assessment_partner_id: int
    category_master_id: int
    test_url: str
    user_id: str
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True
