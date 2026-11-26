//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlinfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlinfo.h>
#include <QtCore/qchar.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qtextstream.h>
#include <QtCore/qurl.h>

//  QQmlInfo::QQmlInfo(const QQmlInfo &a0)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfoC1ERKS_(const QQmlInfo *a0) {
  return new QQmlInfo(*a0);
}

//  QQmlInfo::~QQmlInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlInfoD1Ev(QQmlInfo *self) {
  delete self;
}

//  QQmlInfo &QQmlInfo::operator<<(QChar t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsE5QChar(QQmlInfo *self, const QChar *t) {
  return &(self->operator<<(*t));
}

//  QQmlInfo &QQmlInfo::operator<<(bool t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsEb(QQmlInfo *self, bool t) {
  return &(self->operator<<(t));
}

//  QQmlInfo &QQmlInfo::operator<<(char t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsEc(QQmlInfo *self, char t) {
  return &(self->operator<<(t));
}

//  QQmlInfo &QQmlInfo::operator<<(short t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsEs(QQmlInfo *self, short t) {
  return &(self->operator<<(t));
}

//  QQmlInfo &QQmlInfo::operator<<(unsigned short t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsEt(QQmlInfo *self, unsigned short t) {
  return &(self->operator<<(t));
}

//  QQmlInfo &QQmlInfo::operator<<(int t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsEi(QQmlInfo *self, int t) {
  return &(self->operator<<(t));
}

//  QQmlInfo &QQmlInfo::operator<<(unsigned int t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsEj(QQmlInfo *self, unsigned int t) {
  return &(self->operator<<(t));
}

//  QQmlInfo &QQmlInfo::operator<<(long t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsEl(QQmlInfo *self, long t) {
  return &(self->operator<<(t));
}

//  QQmlInfo &QQmlInfo::operator<<(unsigned long t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsEm(QQmlInfo *self, unsigned long t) {
  return &(self->operator<<(t));
}

//  QQmlInfo &QQmlInfo::operator<<(qint64 t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsEx(QQmlInfo *self, qint64 t) {
  return &(self->operator<<(t));
}

//  QQmlInfo &QQmlInfo::operator<<(quint64 t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsEy(QQmlInfo *self, quint64 t) {
  return &(self->operator<<(t));
}

//  QQmlInfo &QQmlInfo::operator<<(float t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsEf(QQmlInfo *self, float t) {
  return &(self->operator<<(t));
}

//  QQmlInfo &QQmlInfo::operator<<(double t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsEd(QQmlInfo *self, double t) {
  return &(self->operator<<(t));
}

//  QQmlInfo &QQmlInfo::operator<<(const char *t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsEPKc(QQmlInfo *self, const char *t) {
  return &(self->operator<<(t));
}

//  QQmlInfo &QQmlInfo::operator<<(const QString &t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsERK7QString(QQmlInfo *self, const QString *t) {
  return &(self->operator<<(*t));
}

//  QQmlInfo &QQmlInfo::operator<<(QStringView t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsE11QStringView(
    QQmlInfo *self,
    const QString *t) {
  return &(self->operator<<(QStringView(*t)));
}

//  QQmlInfo &QQmlInfo::operator<<(const QLatin1String &t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsERK13QLatin1String(
    QQmlInfo *self,
    const QLatin1String *t) {
  return &(self->operator<<(*t));
}

//  QQmlInfo &QQmlInfo::operator<<(const QByteArray &t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsERK10QByteArray(
    QQmlInfo *self,
    const QByteArray *t) {
  return &(self->operator<<(*t));
}

//  QQmlInfo &QQmlInfo::operator<<(const void *t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsEPKv(QQmlInfo *self, const void *t) {
  return &(self->operator<<(t));
}

//  QQmlInfo &QQmlInfo::operator<<(QTextStreamFunction f)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsEPFR11QTextStreamS1_E(
    QQmlInfo *self,
    void *f) {
  return &(self->operator<<(reinterpret_cast<QTextStreamFunction>(f)));
}

//  QQmlInfo &QQmlInfo::operator<<(QTextStreamManipulator m)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsE22QTextStreamManipulator(
    QQmlInfo *self,
    const QTextStreamManipulator *m) {
  return &(self->operator<<(*m));
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QQmlInfo &QQmlInfo::operator<<(const QUrl &t)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfolsERK4QUrl(QQmlInfo *self, const QUrl *t) {
  return &(self->operator<<(*t));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QQmlInfo::QQmlInfo(QQmlInfoPrivate *a0)
extern "C" Q_DECL_EXPORT
QQmlInfo *ritual_ZN8QQmlInfoC1EP15QQmlInfoPrivate(QQmlInfoPrivate *a0) {
  return new QQmlInfo(a0);
}
