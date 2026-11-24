//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qxml.h>
#include <QtCore/qstring.h>

//  QXmlParseException::QXmlParseException(const QString &name, int c, int l,
//      const QString &p, const QString &s)
extern "C" Q_DECL_EXPORT
QXmlParseException *ritual_ZN18QXmlParseExceptionC1ERK7QStringiiS2_S2_(
    const QString *name,
    int c,
    int l,
    const QString *p,
    const QString *s) {
  return new QXmlParseException(*name, c, l, *p, *s);
}

//  QXmlParseException::QXmlParseException(const QXmlParseException &other)
extern "C" Q_DECL_EXPORT
QXmlParseException *ritual_ZN18QXmlParseExceptionC1ERKS_(
    const QXmlParseException *other) {
  return new QXmlParseException(*other);
}

//  QXmlParseException::~QXmlParseException()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QXmlParseExceptionD1Ev(QXmlParseException *self) {
  delete self;
}

//  int QXmlParseException::columnNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QXmlParseException12columnNumberEv(
    const QXmlParseException *self) {
  return self->columnNumber();
}

//  int QXmlParseException::lineNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QXmlParseException10lineNumberEv(
    const QXmlParseException *self) {
  return self->lineNumber();
}

//  QString QXmlParseException::publicId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QXmlParseException8publicIdEv(
    const QXmlParseException *self) {
  return new QString(self->publicId());
}

//  QString QXmlParseException::systemId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QXmlParseException8systemIdEv(
    const QXmlParseException *self) {
  return new QString(self->systemId());
}

//  QString QXmlParseException::message() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QXmlParseException7messageEv(
    const QXmlParseException *self) {
  return new QString(self->message());
}
