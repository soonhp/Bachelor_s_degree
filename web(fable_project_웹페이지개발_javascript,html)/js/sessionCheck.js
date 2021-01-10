var addressss = window.location.href.split("/")[3]
if(addressss == "mypage.html") {
  //유저가 로그인 했는지 안했는지 확인해주는 함수
  function userSessionCheck() {
    console.log(currentTime);
    //로그인이 되어있으면 - 유저가 있으면, user를 인자값으로 넘겨준다.
    firebaseEmailAuth.onAuthStateChanged(function (user) {
      if (user) {
        firebaseDatabase.ref("users/" + user.uid).once('value').then(function (snapshot) {
          document.getElementById("loginmenu").textContent = "로그아웃";
          document.getElementById("loginmenu").href = "/logout.html";
          document.getElementById("joinmenu").textContent = "반가워요! " + snapshot.val().name + " 님";
          document.getElementById("joinmenu").href = "#";
  
          name = snapshot.val().name;   //유저 닉네임은 계속 쓸거기 때문에 전역변수로 할당
          loginUserKey = snapshot.key;  //로그인한 유저의 key도 계속 쓸 것이기 때문에 전역변수로 할당
          userInfo = snapshot.val(); //snapshot.val()에 user 테이블에 있는 해당 개체 정보가 넘어온다. userInfo에 대입!
              
              
              //이부분까지 index.html에 해당하는 로직 이후에 엘리멘트 id로 mypage인지 메인 페이지인지 구분
              //mypage에서 호출했다면
          if(document.getElementById("titleCheck").textContent=="mypage"){
            document.getElementById("nicname").textContent = name
            if (snapshot.val().imgURl) {
              document.getElementById("myimage").src = snapshot.val().imgURl
              console.log("이미지가 저장되어 있네요");  
            } else {
              document.getElementById("myimage").src = "https://www.w3schools.com/bootstrap/img_avatar3.png";
              console.log("이미지가 없네요ㅠㅠ");
            }
            if (snapshot.val().comment) {
              document.getElementById("statetxt").textContent = snapshot.val().comment;
              console.log("한줄글이 저장되어 있네요");
            } else {
              document.getElementById("statetxt").textContent = "한줄 기분을 적고 프로필 사진을 선택해 주세요~";
              console.log("한줄글이 없네요 ㅠㅠ");
            }
          } else {
            thanksList();
            return true
          }
        });
      } else {
         alert("로그인 해주세요.")
         window.location = '/login.html'
         return;
        }
      });
    }
  } else {
     var address = window.location.href.split("?")[1]
     var addresss = address.split("=")[1]
     function userSessionCheck() {
       console.log(currentTime);
       firebaseEmailAuth.onAuthStateChanged(function (user) {
         if (user) {
           firebaseDatabase.ref("users/" + user.uid).once('value').then(function (snapshot) {
             document.getElementById("joinmenu").textContent = "반가워요! " + snapshot.val().name + " 님";
           });
           firebaseDatabase.ref("users/" + addresss).once('value').then(function (snapshot) {
             document.getElementById("loginmenu").textContent = "로그아웃";
             document.getElementById("loginmenu").href = "/logout.html";
             document.getElementById("joinmenu").href = "#";
             name = snapshot.val().name;   //유저 닉네임은 계속 쓸거기 때문에 전역변수로 할당
             loginUserKey = snapshot.key;  //로그인한 유저의 key도 계속 쓸 것이기 때문에 전역변수로 할당
             userInfo = snapshot.val(); //snapshot.val()에 user 테이블에 있는 해당 개체 정보가 넘어온다. userInfo에 대입!
             if(document.getElementById("titleCheck").textContent=="mypage"){
               document.getElementById("nicname").textContent = name
               if (snapshot.val().imgURl) {
                 document.getElementById("myimage").src = snapshot.val().imgURl
                 console.log("이미지가 저장되어 있네요");
                } else {
                  document.getElementById("myimage").src = "https://www.w3schools.com/bootstrap/img_avatar3.png";
                  console.log("이미지가 없네요ㅠㅠ");
                }
                if (snapshot.val().comment) {
                  document.getElementById("statetxt").textContent = snapshot.val().comment;
                  console.log("한줄글이 저장되어 있네요");
                } else {
                  document.getElementById("statetxt").textContent = "한줄 기분을 적고 프로필 사진을 선택해 주세요~";
                  console.log("한줄글이 없네요 ㅠㅠ");
                }
              } else {
                thanksList();
                return true
                }
              });
            } else {
              alert("로그인 해주세요.")
              window.location = '/login.html'
              return;
            }
          });
        }
      
      }