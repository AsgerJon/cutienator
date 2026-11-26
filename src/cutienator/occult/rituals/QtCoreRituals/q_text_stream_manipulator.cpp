//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtextstream.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, rituals for functions the generator leaves out: 2. Kept as it is
//  when the generator runs again.
#include <QtCore/qtextstream.h>
#include <cstring>

//  void QTextStreamManipulator::exec(QTextStream &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QTextStreamManipulator4execER11QTextStream(
    QTextStreamManipulator *self,
    QTextStream *s) {
  self->exec(*s);
}

//  QTextStreamManipulator::~QTextStreamManipulator()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QTextStreamManipulatorD1Ev(QTextStreamManipulator *self) {
  delete self;
}

//  QTextStreamManipulator::QTextStreamManipulator(QTSMFI m, int a)
extern "C" Q_DECL_EXPORT
QTextStreamManipulator *ritual_ZN22QTextStreamManipulatorC2EM11QTextStreamFviEi(
    const char *m,
    int a) {
  static const struct {
    const char *name;
    QTSMFI member;
  } known[] = {
      {"setFieldWidth", &QTextStream::setFieldWidth},
      {"setIntegerBase", &QTextStream::setIntegerBase},
      {"setRealNumberPrecision", &QTextStream::setRealNumberPrecision},
  };
  for (const auto &one : known) {
    if (!std::strcmp(one.name, m)) {
      return new QTextStreamManipulator(one.member, a);
    }
  }
  qFatal("no member function named %s here", m);
}

//  QTextStreamManipulator::QTextStreamManipulator(QTSMFC m, QChar c)
extern "C" Q_DECL_EXPORT
QTextStreamManipulator *ritual_ZN22QTextStreamManipulatorC2EM11QTextStreamFv5QCharES1_(
    const char *m,
    const QChar *c) {
  static const struct {
    const char *name;
    QTSMFC member;
  } known[] = {
      {"setPadChar", &QTextStream::setPadChar},
  };
  for (const auto &one : known) {
    if (!std::strcmp(one.name, m)) {
      return new QTextStreamManipulator(one.member, *c);
    }
  }
  qFatal("no member function named %s here", m);
}
