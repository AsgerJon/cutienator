//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstream)
#include <QtCore/qxmlstream.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  QtPrivate::QXmlString::QXmlString(QStringPrivate &&d)
extern "C" Q_DECL_EXPORT
QtPrivate::QXmlString *ritual_ZN9QtPrivate10QXmlStringC1EO17QArrayDataPointerIDsE(
    QStringPrivate *d) {
  return new QtPrivate::QXmlString(std::move(*d));
}

//  QtPrivate::QXmlString::QXmlString(const QString &s)
extern "C" Q_DECL_EXPORT
QtPrivate::QXmlString *ritual_ZN9QtPrivate10QXmlStringC1ERK7QString(
    const QString *s) {
  return new QtPrivate::QXmlString(*s);
}

//  QXmlString &QtPrivate::QXmlString::operator=(const QString &s)
extern "C" Q_DECL_EXPORT
QtPrivate::QXmlString *ritual_ZN9QtPrivate10QXmlStringaSERK7QString(
    QtPrivate::QXmlString *self,
    const QString *s) {
  return &(self->operator=(*s));
}

//  QXmlString &QtPrivate::QXmlString::operator=(QString &&s)
extern "C" Q_DECL_EXPORT
QtPrivate::QXmlString *ritual_ZN9QtPrivate10QXmlStringaSEO7QString(
    QtPrivate::QXmlString *self,
    QString *s) {
  return &(self->operator=(std::move(*s)));
}

//  QtPrivate::QXmlString::QXmlString()
extern "C" Q_DECL_EXPORT
QtPrivate::QXmlString *ritual_ZN9QtPrivate10QXmlStringC1Ev() {
  return new QtPrivate::QXmlString();
}

//  void QtPrivate::QXmlString::swap(QXmlString &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate10QXmlString4swapERS0_(
    QtPrivate::QXmlString *self,
    QtPrivate::QXmlString *other) {
  self->swap(*other);
}

//  QStringView QtPrivate::QXmlString::operator QStringView() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QtPrivate10QXmlStringcv11QStringViewEv(
    const QtPrivate::QXmlString *self) {
  return new QString(self->operator QStringView().toString());
}

//  qsizetype QtPrivate::QXmlString::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK9QtPrivate10QXmlString4sizeEv(
    const QtPrivate::QXmlString *self) {
  return self->size();
}

//  bool QtPrivate::QXmlString::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate10QXmlString6isNullEv(
    const QtPrivate::QXmlString *self) {
  return self->isNull();
}

//  bool operator==(const QXmlString &lhs, const QXmlString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateeqERKNS_10QXmlStringES2_(
    const QtPrivate::QXmlString *lhs,
    const QtPrivate::QXmlString *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QXmlString &lhs, const QXmlString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateneERKNS_10QXmlStringES2_(
    const QtPrivate::QXmlString *lhs,
    const QtPrivate::QXmlString *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QtPrivate::QXmlString::~QXmlString()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate10QXmlStringD1Ev(QtPrivate::QXmlString *self) {
  delete self;
}

#endif  // QT_CONFIG(xmlstream)
#endif  // QT_CONFIG(xmlstream)
