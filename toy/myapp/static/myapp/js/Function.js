function createStr() {
    if(/*나이값 없으면*/ false) document.write("나이를 입력해주세요!");
    else if(/*성별값 없으면*/ false) document.write("성별");
    else if(/*미팅 인원수*/ false) document.write("원하는 미팅 인원수");
    else if(/*직업*/ false) document.write("직업"); //대학생, 대학원생, 취준생, 직장인
    else if(/*대학생이면*/ false) document.write("학교와 학과"); //학교 인증 시스템 넣기
    else if(/*mbti*/ false) document.write("mbti");
    else if(/*남자면*/ false) document.write("군/미필");
    else if(/*키*/ false) document.write("키"); //범위로(5단위)
    else if(/*체형*/ false) document.write("체형"); //탭으로(마름, 보통, 통통, 근육)
    else if(/*유/무쌍*/ false) document.write("유/무쌍"); //탭으로
    else if(/*얼굴상*/ false) document.write("얼굴상"); //뚜렷, 두부
    else if(/*관심사*/ false) document.write("관심사"); //탭으로
    else if(/*자유로운 자기소개*/ true) {
        document.write("자유로운 자기소개<br>");
        document.write("최소 10자의 자기소개를 적어주세요.<br>");
        document.write("자기소개를 길게 쓸수록 <br> 매칭확률이 높아집니다.");
    }
} 
function create() {
    const elem= document.getElementById("form");
    if(/*나이값 없으면*/ false) {
        elem.innerHTML = "<input type=text id=input1 size=10 required></input>"
    }
    else if(/*성별값 없으면*/ false) {
        elem.innerHTML = "<input type=radio name=sex id=male required> <label for=male> 남성 </label>\
                <input type=radio name=sex id=female required> <label for=female> 여성 </label>"
    }
    else if(/*미팅 인원수*/ false) {
        elem.innerHTML = "<input type=checkbox id=one value=1 > <label for = one> 소개팅 </label> \
                <input type=checkbox id=two value=2 required> <label for = two> 2명이서 </label>\
                <input type=checkbox id=three value=3 > <label for = three> 3명이서 </label> \
                <input type=checkbox id=four value=4 > <label for = four> 4명이서 </label> "
    }
    else if(/*직업*/ false) {
        elem.innerHTML = "<input type=radio name=job id=1  > <label for = 1> 대학생 </label> \
                 <input type=radio name=job id=2 value=대학원생> <label for = 2> 대학원생 </label> \
                 <input type=radio name=job id=3 value=취준생 > <label for = 3> 취준생 </label> \
                 <input type=radio name=job id=4 value=직장인 > <label for = 4> 직장인 </label> "
    }
    else if(/*대학생이면*/ true) {
        elem.innerHTML = "<input type=text placeholder=학교 size=10 required></input>\
        <br><br>\
        <input type=radio id=1 name=major value=문과대 > <label for = 1> 문과대 </label>\
        <input type=radio id=2 name=major value=이과대> <label for = 2> 이과대 </label>\
        <input type=radio id=3 name=major value=사범대 > <label for = 3> 사범대 </label>\
        <input type=radio id=4 name=major value=체대> <label for = 4> 체대 </label>\
        <input type=radio id=5 name=major value=미대> <label for = 5> 미대 </label>\
        <input type=radio id=6 name=major value=예대> <label for = 6> 예대 </label>\
        <input type=radio id=7 name=major value=음대> <label for = 7> 음대 </label>\
        <input type=radio id=8 name=major value=의약대> <label for = 8> 의/약대 </label>\
        <input type=radio id=9 name=major value=특수대> <label for = 9> 특수대 </label> "
    }
    else if(/*mbti*/ false) {
        elem.innerHTML = "<input type=text size=10 required></input>"
    }
    else if(/*남자면*/ false) {
        elem.innerHTML = "<input type=radio id=1 name=army value=군필 > <label for=1> 군필 </label> \
                <input type=radio id=2 name=army value=미필 required> <label for=2> 미필 </label>"
    }
    else if(/*키*/ true) {
        elem.innerHTML = "\
        <form class=box> \
            <div class=slider>\
              <input type=range id=input-left min=1 max=100 value=1 oninput=document.getElementById('output1').innerHTML=this.value;/> \
              <input type=range id=input-right min=1 max=100 value=100 oninput=document.getElementById('output2').innerHTML=this.value;/> \
              <div class=track>\
                <div class=range></div>\
                <div class=thumb left></div>\
                <div class=thumb right></div>\
              </div>\
            </div>\
            <span id=output1></span> <span>~</span> <span id=output2></span>\
        </form>"
    }
    else if(/*체형*/ false) {
        elem.innerHTML = "<input type=radio id=1 name=body value=마름 > <label for = 1> 마름 </label> \
                <input type=radio id=2 name=body value=보통> <label for = 2>  보통 </label>\
                <input type=radio id=3 name=body value=통통 > <label for = 3>  통통 </label> \
                <input type=radio id=4 name=body value=탄탄> <label for = 4>  탄탄 </label>"
    }
    else if(/*유무쌍*/ false) {
        elem.innerHTML = "<input type=radio id=1 name=eyes value=유쌍 > <label for = 1> 유쌍 </label> \
        <input type=radio id=2 name=eyes value=무쌍> <label for = 2>  무쌍 </label>"
    }
    else if(/*얼굴상*/ false) {
        elem.innerHTML = "<input type=radio id=1 name=face value=두부 > <label for = 1> 두부상 </label> \
        <input type=radio id=2 name=face value=뚜렷> <label for = 2> 뚜렷상 </label>"
    }
   
    else if(/*관심사*/ false) {
        elem.innerHTML = "<input type=checkbox id=1 value=1 > <label for = 1> 운동 </label> \
                <input type=checkbox id=2 value=2 required> <label for = 2> 산책 </label>\
                <input type=checkbox id=3 value=3 > <label for = 3> 공연관람 </label> \
                <input type=checkbox id=4 value=4 > <label for = 4> 쇼핑 </label> \
                <input type=checkbox id=5 value=1 > <label for = 5> 재태크 </label> \
                <input type=checkbox id=6 value=2 required> <label for = 6> 패션 </label>\
                <input type=checkbox id=7 value=3 > <label for = 7> 반려동물 </label> \
                <input type=checkbox id=8 value=4 > <label for = 8> 음악감상 </label>\
                <input type=checkbox id=9 value=1 > <label for = 9> 독서 </label> \
                <input type=checkbox id=10 value=2 required> <label for = 10> 여행 </label>\
                <input type=checkbox id=11 value=3 > <label for = 11> 카페 </label> \
                <input type=checkbox id=12 value=4 > <label for = 12> 게임 </label>\
                <input type=checkbox id=13 value=2 required> <label for = 13> 영화/드라마 </label>\
                <input type=checkbox id=14 value=3 > <label for = 14> 전시관람 </label> \
                <input type=checkbox id=15 value=4 > <label for = 15> 연극/뮤지컬 </label>\
                <input type=checkbox id=16 value=1 > <label for = 16> 술 </label> \
                <input type=checkbox id=17 value=2 required> <label for = 17> 악기연주 </label>\
                <input type=checkbox id=18 value=3 > <label for = 18> 맛집 </label> \
                <input type=checkbox id=19 value=4 > <label for = 19> 요리 </label>"
    }
    else if(/*자유로운 자기소개*/ true) {
        elem.innerHTML = "<br> <textarea id=input2 cols=40 rows=10> </textarea>"
    }
}

function ageLevel() {
    const elem= document.getElementById("form1");
    elem.innerHTML = "<p>매칭하길 원하는 나이대를 선택해주세요(다수선택 가능)</p> \
    <label> <input type=checkbox> 20살 \
    <input type=checkbox> 21살 \
    <input type=checkbox> 22살 \
    <input type=checkbox> 23살 \
    <input type=checkbox> 24살 \
    <input type=checkbox> 25살 \
    <input type=checkbox> 26살 \
    <input type=checkbox> 27살 \
    <input type=checkbox> 28살 \
    <input type=checkbox> 29살 \
     </label> "
}

function job() {
    const elem= document.getElementById("form2");
    elem.innerHTML = " <p>원하는 상대방의 직업을 선택해주세요(다수선택 가능)</p>\
    <label> <input type=checkbox value=대학생 > 대학생 </label> \
                <label> <input type=checkbox value=대학원생> 대학원생 </label> \
                <label> <input type=checkbox value=취준생 > 취준생 </label> \
                <label> <input type=checkbox value=직장인 > 직장인 </label> "
}

function major() {
    const elem= document.getElementById("form0");
    elem.innerHTML = "<input type=text id=input placeholder=학과 size=10 required></input> "
}