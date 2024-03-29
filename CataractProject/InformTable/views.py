from django.shortcuts import render, redirect
from InformTable.models import PersonalInformation, EssentialInformation, DoctorLogin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def postdiagnose(request):
    info = PersonalInformation()
    info2 = EssentialInformation()
    if request.POST:
        info.id = request.POST.get("id")
        info.name = request.POST.get("name")
        info.age = request.POST.get("age")
        info.sex = request.POST.get("sex")
        info.nation = request.POST.get("nation")
        info.marriage = request.POST.get("marriage")
        info.occupation = request.POST.get("occupation")
        info.p_birthplace = request.POST.get("p_birthplace")
        info.address = request.POST.get("address")
        info.medicalhistory_reporter = request.POST.get("medicalhistory_reporter")
        info.admission_date = request.POST.get("admission_date")
        info.medicalhistory_recordtime = request.POST.get("medicalhistory_recordtime")
        info.save()

        info2.id = request.POST.get("id")
        info2.main_suit = request.POST.get("main_suit")
        info2.medicalhistory_present = request.POST.get("medicalhistory_present")
        info2.tuberculosis_history = request.POST.get("tuberculosis_history")
        info2.hepatitis_history = request.POST.get("hepatitis_history")
        info2.other_infectious_diseases_history = request.POST.get("other_infectious_diseases_history")
        info2.hypertension_history = request.POST.get("hypertension_history")
        info2.diabetes_mellitus_history = request.POST.get("diabetes_mellitus_history")
        info2.chronic_disease_history = request.POST.get("chronic_disease_history")
        info2.heart_disease_history = request.POST.get("heart_disease_history")
        info2.vaccination_allergy_history = request.POST.get("vaccination_allergy_history")
        info2.surgery_history = request.POST.get("surgery_history")
        info2.past_history_remarks = request.POST.get("past_history_remarks")
        info2.e_birthplace = request.POST.get("e_birthplace")
        info2.smoking_hobbies = request.POST.get("smoking_hobbies")
        info2.drinking_hobbies = request.POST.get("drinking_hobbies")
        info2.epidemic_water_contact_history = request.POST.get("epidemic_water_contact_history")
        info2.personal_history_remark = request.POST.get("personal_history_remark")
        info2.marriage_history = request.POST.get("marriage_history")
        info2.marital_reproductive_history_remark = request.POST.get("marital_reproductive_history_remark")
        info2.menopause = request.POST.get("menopause")
        info2.menstrual_history_remark = request.POST.get("menstrual_history_remark")
        info2.diabetes_mellitus_family_history = request.POST.get("diabetes_mellitus_family_history")
        info2.coronary_heart_disease_family_history = request.POST.get("coronary_heart_disease_family_history")
        info2.stroke_family_history = request.POST.get("stroke_family_history")
        info2.tumors_family_history = request.POST.get("tumors_family_history")
        info2.hypertension_family_history = request.POST.get("hypertension_family_history")
        info2.family_history_remark = request.POST.get("family_history_remark")
        info2.save()
    return render(request, "DetailInform.html")


@login_required
def showpatientlist(request):
    patientlist = PersonalInformation.objects.all()
    return render(request, "PatientsList.html", {"p_list": patientlist})


@login_required
def deletediagnose(request, id):
    personal_info_obj = PersonalInformation.objects
    essential_info_obj = EssentialInformation.objects
    personal_info_obj.filter(id=id).delete()
    essential_info_obj.filter(id=id).delete()
    return redirect("/patientslist")


@login_required
def editdiagnose(request, id):
    personal_info = PersonalInformation.objects.get(id=id)
    essential_info = EssentialInformation.objects.get(id=id)
    if request.method == "GET":
        return render(request, "EditInform.html", {"personal_info": personal_info, "essential_info": essential_info})
    else:

        # part 1
        name = request.POST.get("name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        nation = request.POST.get("nation")
        marriage = request.POST.get("marriage")
        occupation = request.POST.get("occupation")
        p_birthplace = request.POST.get("p_birthplace")
        address = request.POST.get("address")
        medicalhistory_reporter = request.POST.get("medicalhistory_reporter")

        p_info = PersonalInformation.objects.filter(id=id)  # 返回的是一个对象列表,QuerySet

        p_info.update(age=age)
        p_info.update(name=name)
        p_info.update(sex=sex)
        p_info.update(nation=nation)
        p_info.update(marriage=marriage)
        p_info.update(occupation=occupation)
        p_info.update(p_birthplace=p_birthplace)
        p_info.update(address=address)
        p_info.update(medicalhistory_reporter=medicalhistory_reporter)

        # part 2
        main_suit = request.POST.get("main_suit")
        medicalhistory_present = request.POST.get("medicalhistory_present")
        tuberculosis_history = request.POST.get("tuberculosis_history")
        hepatitis_history = request.POST.get("hepatitis_history")
        other_infectious_diseases_history = request.POST.get("other_infectious_diseases_history")
        hypertension_history = request.POST.get("hypertension_history")
        diabetes_mellitus_history = request.POST.get("diabetes_mellitus_history")
        chronic_disease_history = request.POST.get("chronic_disease_history")
        heart_disease_history = request.POST.get("heart_disease_history")
        vaccination_allergy_history = request.POST.get("vaccination_allergy_history")
        surgery_history = request.POST.get("surgery_history")
        past_history_remarks = request.POST.get("past_history_remarks")
        e_birthplace = request.POST.get("e_birthplace")
        smoking_hobbies = request.POST.get("smoking_hobbies")
        drinking_hobbies = request.POST.get("drinking_hobbies")
        epidemic_water_contact_history = request.POST.get("epidemic_water_contact_history")
        personal_history_remark = request.POST.get("personal_history_remark")
        marriage_history = request.POST.get("marriage_history")
        marital_reproductive_history_remark = request.POST.get("marital_reproductive_history_remark")
        menopause = request.POST.get("menopause")
        menstrual_history_remark = request.POST.get("menstrual_history_remark")
        diabetes_mellitus_family_history = request.POST.get("diabetes_mellitus_family_history")
        coronary_heart_disease_family_history = request.POST.get("coronary_heart_disease_family_history")
        stroke_family_history = request.POST.get("stroke_family_history")
        tumors_family_history = request.POST.get("tumors_family_history")
        hypertension_family_history = request.POST.get("hypertension_family_history")
        family_history_remark = request.POST.get("family_history_remark")

        e_info = EssentialInformation.objects.filter(id=id)

        e_info.update(main_suit=main_suit)
        e_info.update(medicalhistory_present=medicalhistory_present)
        e_info.update(tuberculosis_history=tuberculosis_history)
        e_info.update(hepatitis_history=hepatitis_history)
        e_info.update(other_infectious_diseases_history=other_infectious_diseases_history)
        e_info.update(hypertension_history=hypertension_history)
        e_info.update(diabetes_mellitus_history=diabetes_mellitus_history)
        e_info.update(chronic_disease_history=chronic_disease_history)
        e_info.update(heart_disease_history=heart_disease_history)
        e_info.update(vaccination_allergy_history=vaccination_allergy_history)
        e_info.update(surgery_history=surgery_history)
        e_info.update(past_history_remarks=past_history_remarks)
        e_info.update(e_birthplace=e_birthplace)
        e_info.update(smoking_hobbies=smoking_hobbies)
        e_info.update(drinking_hobbies=drinking_hobbies)
        e_info.update(epidemic_water_contact_history=epidemic_water_contact_history)
        e_info.update(personal_history_remark=personal_history_remark)
        e_info.update(marriage_history=marriage_history)
        e_info.update(marital_reproductive_history_remark=marital_reproductive_history_remark)
        e_info.update(menopause=menopause)
        e_info.update(menstrual_history_remark=menstrual_history_remark)
        e_info.update(diabetes_mellitus_family_history=diabetes_mellitus_family_history)
        e_info.update(coronary_heart_disease_family_history=coronary_heart_disease_family_history)
        e_info.update(stroke_family_history=stroke_family_history)
        e_info.update(tumors_family_history=tumors_family_history)
        e_info.update(hypertension_family_history=hypertension_family_history)
        e_info.update(family_history_remark=family_history_remark)

        return redirect('/patientslist')


def doctorsignup(request):
    state = ""
    if request.method == 'POST':
        username = request.POST.get('docid', '') # 相当于django自带user验证的username
        hosid = request.POST.get('hosid', '')
        hosname = request.POST.get('hosname', '')
        password = request.POST.get('docpwd', '') #相当于django自带user验证的password
        docname = request.POST.get('docname', '')
        repeat_password = request.POST.get('repeat_docpwd', '')

        if DoctorLogin.objects.filter(username=username):
            state = '用户已存在'
        else:
            new_user = DoctorLogin.objects.create_user(username=username, password=password, hosid=hosid, hosname=hosname, docname=docname)
            new_user.save()

            return redirect('/doctorlogin/')

    return render(request, 'DoctorSignUp.html', {'state': state, 'user': None})


def doctorlogin(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get('docid')
        password = request.POST.get('docpwd')
        user = authenticate(username=username, password=password) # 其他字段对这个没影响
        if user is not None:
            login(request, user)
            return redirect('/patientslist/')
        else:
            message = "用户名或密码错误,请重新输入"
    return render(request, "DoctorLogin.html", {"message": message})


@login_required
def doctorlogout(request):
    logout(request)
    return redirect('/doctorlogin/')
