import 'package:flutter/material.dart';

void main() {
  runApp(const TtlFieldApp());
}

class TtlFieldApp extends StatelessWidget {
  const TtlFieldApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'TTL Field',
      theme: ThemeData(useMaterial3: true),
      home: const Scaffold(
        body: Center(
          child: Text('TTL Field Telemetria em background'),
        ),
      ),
    );
  }
}
