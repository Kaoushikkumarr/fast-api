"""
This File mainly created for creating Data Base Model of this project.
"""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from infrastructure.database import Base


class Assessment(Base):
    __tablename__ = "assessment"

    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False, autoincrement=True)
    slug = Column(String)
    total_candidates = Column(Integer)


class UserInformation(Base):
    __tablename__ = 'user_information'

    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False, autoincrement=True)
    user_name = Column(String(120), index=False, unique=True)
    password = Column(String(120), index=False, unique=False)
    email = Column(String(120), index=False, unique=True)


class Tenant(Base):
    __tablename__ = 'tenant'

    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False, autoincrement=True)
    tenant_name = Column(String(120), index=False, unique=True)
    status = Column(Boolean, nullable=True)
    user_id = Column(String(120), index=False, unique=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())


class SkillMaster(Base):
    __tablename__ = 'skill_master'

    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False, autoincrement=True)
    skill_name = Column(String(120), index=False, unique=True)
    user_id = Column(String(120), index=False, unique=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())


class PartnerType(Base):
    __tablename__ = 'partner_type'

    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False, autoincrement=True)
    partner_name = Column(String(120), index=False, unique=True)
    user_id = Column(String(120), index=False, unique=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())


class ApplicationMaster(Base):
    __tablename__ = 'application_master'

    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False, autoincrement=True)
    application_name = Column(String(120), index=False, unique=True)
    user_id = Column(String(120), index=False, unique=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())


class AssessmentMaster(Base):
    __tablename__ = 'assessment_master'

    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False, autoincrement=True)
    test_id = Column(String(120), index=False, unique=True)
    user_id = Column(String(120), index=False, unique=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())


class CategoryMaster(Base):
    __tablename__ = 'category_master'

    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False, autoincrement=True)
    category_type = Column(String(120), index=False, unique=True)
    user_id = Column(String(120), index=False, unique=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())


class AssessmentPartner(Base):
    __tablename__ = 'assessment_partner'

    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False, autoincrement=True)
    partner_name = Column(String(120), index=False, unique=True)
    partner_type = Column(Integer, ForeignKey("partner_type.id"))
    status = Column(Boolean, default=True)
    subscription_key = Column(String(120), index=False, unique=False)
    subscription_password = Column(String(120), index=False, unique=False)
    user_id = Column(String(120), index=False, unique=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())


class SubscriptionMaster(Base):
    __tablename__ = 'subscription_master'

    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False, autoincrement=True)
    tenant_id = Column(Integer, ForeignKey("tenant.id"))
    partner_id = Column(Integer, ForeignKey("assessment_partner.id"))
    subscription = Column(Boolean, nullable=True)
    user_id = Column(String(120), index=False, unique=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())


class AssessmentMapping(Base):
    __tablename__ = 'assessment_mapping'

    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False, autoincrement=True)
    test_id = Column(String(120), index=False, unique=True)
    application_master_id = Column(Integer, ForeignKey("application_master.id"))
    skill_master_id = Column(Integer, ForeignKey("skill_master.id"))
    assessment_partner_id = Column(Integer, ForeignKey("assessment_partner.id"))
    category_master_id = Column(Integer, ForeignKey("category_master.id"))
    test_url = Column(String(512), index=False, unique=False)
    user_id = Column(String(120), index=False, unique=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())
