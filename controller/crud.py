"""
Under this file all the CRUD(GET, POST, PUT, DELETE) applications will be performed.
"""
from fastapi import HTTPException, status
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from schema_mapping import schemas
from model import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # password encrypting here


def create_assessment(assessment: schemas.Assessment, db: Session):
    db_assessment = models.Assessment(
        slug=assessment.slug,
        total_candidates=assessment.total_candidates
    )
    db.add(db_assessment)
    db.commit()
    db.refresh(db_assessment)
    return db_assessment


def create_users(users: schemas.SignUp, db: Session):
    hash_password = pwd_context.hash(users.password)
    data = models.UserInformation(
        user_name=users.user_name,
        password=hash_password,
        email=users.email
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def create_tenant(tenant: schemas.Tenant, db: Session):
    data = models.Tenant(
        tenant_name=tenant.tenant_name,
        status=tenant.status,
        user_id=tenant.user_id,
        created_date=tenant.created_date,
        updated_date=tenant.updated_date
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def create_skill(skill: schemas.SkillMaster, db: Session):
    data = models.SkillMaster(
        user_id=skill.user_id,
        skill_name=skill.skill_name,
        created_date=skill.created_date,
        updated_date=skill.updated_date
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def create_partner(partner: schemas.Partner, db: Session):
    data = models.PartnerType(
        user_id=partner.user_id,
        partner_name=partner.partner_name,
        created_date=partner.created_date,
        updated_date=partner.updated_date
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def create_application(application: schemas.Application, db: Session):
    data = models.ApplicationMaster(
        user_id=application.user_id,
        application_name=application.application_name,
        created_date=application.created_date,
        updated_date=application.updated_date
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def update_application(application_name, application: schemas.Application, db: Session):
    data = db.query(
        models.ApplicationMaster).filter(
        models.ApplicationMaster.application_name == application_name
    ).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Application Name Not Found!')
    data.user_id = application.user_id,
    data.application_name = application.application_name,
    data.updated_date = application.updated_date
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def delete_application(application_name, db: Session):
    data = db.query(
        models.ApplicationMaster).filter(
        models.ApplicationMaster.application_name == application_name
    ).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Application Name Not Found!')
    db.delete(data)
    db.commit()
    return data


def create_category(category: schemas.CategoryMaster, db: Session):
    data = models.CategoryMaster(
        user_id=category.user_id,
        category_type=category.category_type,
        created_date=category.created_date,
        updated_date=category.updated_date
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def update_category(category_type, category: schemas.CategoryMaster, db: Session):
    data = db.query(
        models.CategoryMaster).filter(
        models.CategoryMaster.category_type == category_type
    ).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category Type Not Found!')
    data.user_id = category.user_id,
    data.application_name = category.category_type,
    data.updated_date = category.updated_date
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def delete_category(category_type, db: Session):
    data = db.query(
        models.CategoryMaster).filter(
        models.CategoryMaster.category_type == category_type
    ).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category Type Not Found!')
    db.delete(data)
    db.commit()
    return data


def create_assessment_partner(assessment_partner: schemas.AssessmentPartner, db: Session):
    hash_subscription_key = pwd_context.hash(assessment_partner.subscription_key)
    hash_subscription_password = pwd_context.hash(assessment_partner.subscription_password)
    data = models.AssessmentPartner(
        partner_name=assessment_partner.partner_name,
        partner_type=assessment_partner.partner_type,
        status=assessment_partner.status,
        subscription_key=hash_subscription_key,
        subscription_password=hash_subscription_password,
        user_id=assessment_partner.user_id,
        created_date=assessment_partner.created_date,
        updated_date=assessment_partner.updated_date
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def update_assessment_partner(partner_name, assessment_partner: schemas.AssessmentPartner, db: Session):
    hash_subscription_key = pwd_context.hash(assessment_partner.subscription_key)
    hash_subscription_password = pwd_context.hash(assessment_partner.subscription_password)
    data = db.query(
        models.AssessmentPartner).filter(
        models.AssessmentPartner.partner_name == partner_name
    ).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='AssessmentPartner Not Found!')
    data.partner_name = assessment_partner.partner_name,
    data.partner_type = assessment_partner.partner_type,
    data.status = assessment_partner.status,
    data.subscription_key = hash_subscription_key,
    data.subscription_password = hash_subscription_password,
    data.user_id = assessment_partner.user_id,
    data.created_date = assessment_partner.created_date,
    data.updated_date = assessment_partner.updated_date
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def delete_assessment_partner(partner_name, db: Session):
    data = db.query(
        models.AssessmentPartner).filter(
        models.AssessmentPartner.partner_name == partner_name
    ).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='AssessmentPartner Not Found!')
    db.delete(data)
    db.commit()
    return data


def create_subscription(subscription: schemas.SubscriptionMaster, db: Session):
    data = models.SubscriptionMaster(
        tenant_id=subscription.tenant_id,
        partner_id=subscription.partner_id,
        subscription=subscription.subscription,
        user_id=subscription.user_id,
        created_date=subscription.created_date,
        updated_date=subscription.updated_date
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def create_mapping(mapping: schemas.AssessmentMapping, db: Session):
    data = models.AssessmentMapping(
        test_id=mapping.test_id,
        application_master_id=mapping.application_master_id,
        skill_master_id=mapping.skill_master_id,
        assessment_partner_id=mapping.assessment_partner_id,
        category_master_id=mapping.category_master_id,
        test_url=mapping.test_url,
        user_id=mapping.user_id,
        created_date=mapping.created_date,
        updated_date=mapping.updated_date
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data
