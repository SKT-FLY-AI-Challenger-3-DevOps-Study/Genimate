import 'package:flutter/material.dart';

class MainText extends StatelessWidget {
  const MainText({
    super.key,
  });

  final gradient = const LinearGradient(
    begin: Alignment.topCenter,
    end: Alignment.bottomCenter,
    colors: [Colors.white, Color.fromRGBO(239, 59, 54, 1)],
    stops: [0.2, 0.9],
  );

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        ShaderMask(
          shaderCallback: (Rect bounds) {
            return gradient.createShader(bounds);
          },
          child: const Text(
            'Genimate',
            style: TextStyle(
              color: Colors.white,
              fontSize: 40,
              fontWeight: FontWeight.w500,
            ),
          ),
        ),
        const SizedBox(
          height: 5,
        ),
        const Text(
          "시켜줘. FLYAI 명예 기상캐스터!",
          style: TextStyle(
              color: Color.fromRGBO(239, 59, 54, 1),
              fontSize: 15,
              fontWeight: FontWeight.w500),
        ),
        const SizedBox(
          height: 3,
        ),
        const Text(
          "보라매의 날씨를 메일로 알려주는 서비스입니다.",
          style: TextStyle(
              color: Colors.black87, fontSize: 12, fontWeight: FontWeight.w500),
        ),
        const SizedBox(
          height: 15,
        ),
      ],
    );
  }
}
