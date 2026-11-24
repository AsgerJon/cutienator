//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qxmlstream_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(xmlstream)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qxmlstream_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qxmlstream.h>
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>

//  QtPrivate::XmlStringRef::XmlStringRef()
extern "C" Q_DECL_EXPORT
QtPrivate::XmlStringRef *ritual_ZN9QtPrivate12XmlStringRefC1Ev() {
  return new QtPrivate::XmlStringRef();
}

//  QtPrivate::XmlStringRef::XmlStringRef(const QString *string, qsizetype
//      pos, qsizetype length)
extern "C" Q_DECL_EXPORT
QtPrivate::XmlStringRef *ritual_ZN9QtPrivate12XmlStringRefC1EPK7QStringxx(
    const QString *string,
    qsizetype pos,
    qsizetype length) {
  return new QtPrivate::XmlStringRef(string, pos, length);
}

//  QtPrivate::XmlStringRef::XmlStringRef(const QString *string)
extern "C" Q_DECL_EXPORT
QtPrivate::XmlStringRef *ritual_ZN9QtPrivate12XmlStringRefC1EPK7QString(
    const QString *string) {
  return new QtPrivate::XmlStringRef(string);
}

//  QXmlString QtPrivate::XmlStringRef::operator QXmlString() const
extern "C" Q_DECL_EXPORT
QtPrivate::QXmlString *ritual_ZNK9QtPrivate12XmlStringRefcvNS_10QXmlStringEEv(
    const QtPrivate::XmlStringRef *self) {
  return new QtPrivate::QXmlString(self->operator QtPrivate::QXmlString());
}

//  void QtPrivate::XmlStringRef::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate12XmlStringRef5clearEv(
    QtPrivate::XmlStringRef *self) {
  self->clear();
}

//  QStringView QtPrivate::XmlStringRef::view() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QtPrivate12XmlStringRef4viewEv(
    const QtPrivate::XmlStringRef *self) {
  return new QString(self->view().toString());
}

//  bool QtPrivate::XmlStringRef::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate12XmlStringRef7isEmptyEv(
    const QtPrivate::XmlStringRef *self) {
  return self->isEmpty();
}

//  bool QtPrivate::XmlStringRef::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate12XmlStringRef6isNullEv(
    const QtPrivate::XmlStringRef *self) {
  return self->isNull();
}

//  QString QtPrivate::XmlStringRef::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QtPrivate12XmlStringRef8toStringEv(
    const QtPrivate::XmlStringRef *self) {
  return new QString(self->toString());
}

//  XmlStringRef QtPrivate::XmlStringRef::sliced(qsizetype pos) const
extern "C" Q_DECL_EXPORT
QtPrivate::XmlStringRef *ritual_ZNK9QtPrivate12XmlStringRef6slicedEx(
    const QtPrivate::XmlStringRef *self,
    qsizetype pos) {
  return new QtPrivate::XmlStringRef(self->sliced(pos));
}

//  XmlStringRef QtPrivate::XmlStringRef::sliced(qsizetype pos, qsizetype n)
//      const
extern "C" Q_DECL_EXPORT
QtPrivate::XmlStringRef *ritual_ZNK9QtPrivate12XmlStringRef6slicedExx(
    const QtPrivate::XmlStringRef *self,
    qsizetype pos,
    qsizetype n) {
  return new QtPrivate::XmlStringRef(self->sliced(pos, n));
}

//  qsizetype QtPrivate::XmlStringRef::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK9QtPrivate12XmlStringRef4sizeEv(
    const QtPrivate::XmlStringRef *self) {
  return self->size();
}

//  bool QtPrivate::XmlStringRef::empty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate12XmlStringRef5emptyEv(
    const QtPrivate::XmlStringRef *self) {
  return self->empty();
}

//  bool operator==(const XmlStringRef &lhs, const XmlStringRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateeqERKNS_12XmlStringRefES2_(
    const QtPrivate::XmlStringRef *lhs,
    const QtPrivate::XmlStringRef *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const XmlStringRef &lhs, const XmlStringRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateneERKNS_12XmlStringRefES2_(
    const QtPrivate::XmlStringRef *lhs,
    const QtPrivate::XmlStringRef *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<=(const XmlStringRef &lhs, const XmlStringRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateleERKNS_12XmlStringRefES2_(
    const QtPrivate::XmlStringRef *lhs,
    const QtPrivate::XmlStringRef *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const XmlStringRef &lhs, const XmlStringRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivategeERKNS_12XmlStringRefES2_(
    const QtPrivate::XmlStringRef *lhs,
    const QtPrivate::XmlStringRef *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator<(const XmlStringRef &lhs, const XmlStringRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateltERKNS_12XmlStringRefES2_(
    const QtPrivate::XmlStringRef *lhs,
    const QtPrivate::XmlStringRef *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const XmlStringRef &lhs, const XmlStringRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivategtERKNS_12XmlStringRefES2_(
    const QtPrivate::XmlStringRef *lhs,
    const QtPrivate::XmlStringRef *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator==(const XmlStringRef &lhs, QStringView rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateeqERKNS_12XmlStringRefE11QStringView(
    const QtPrivate::XmlStringRef *lhs,
    const QString *rhs) {
  return operator==(*lhs, QStringView(*rhs));
}

//  bool operator==(QStringView lhs, const XmlStringRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateeqE11QStringViewRKNS_12XmlStringRefE(
    const QString *lhs,
    const QtPrivate::XmlStringRef *rhs) {
  return operator==(QStringView(*lhs), *rhs);
}

//  bool operator!=(const XmlStringRef &lhs, QStringView rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateneERKNS_12XmlStringRefE11QStringView(
    const QtPrivate::XmlStringRef *lhs,
    const QString *rhs) {
  return operator!=(*lhs, QStringView(*rhs));
}

//  bool operator!=(QStringView lhs, const XmlStringRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateneE11QStringViewRKNS_12XmlStringRefE(
    const QString *lhs,
    const QtPrivate::XmlStringRef *rhs) {
  return operator!=(QStringView(*lhs), *rhs);
}

//  bool operator<=(const XmlStringRef &lhs, QStringView rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateleERKNS_12XmlStringRefE11QStringView(
    const QtPrivate::XmlStringRef *lhs,
    const QString *rhs) {
  return operator<=(*lhs, QStringView(*rhs));
}

//  bool operator<=(QStringView lhs, const XmlStringRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateleE11QStringViewRKNS_12XmlStringRefE(
    const QString *lhs,
    const QtPrivate::XmlStringRef *rhs) {
  return operator<=(QStringView(*lhs), *rhs);
}

//  bool operator>=(const XmlStringRef &lhs, QStringView rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivategeERKNS_12XmlStringRefE11QStringView(
    const QtPrivate::XmlStringRef *lhs,
    const QString *rhs) {
  return operator>=(*lhs, QStringView(*rhs));
}

//  bool operator>=(QStringView lhs, const XmlStringRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivategeE11QStringViewRKNS_12XmlStringRefE(
    const QString *lhs,
    const QtPrivate::XmlStringRef *rhs) {
  return operator>=(QStringView(*lhs), *rhs);
}

//  bool operator<(const XmlStringRef &lhs, QStringView rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateltERKNS_12XmlStringRefE11QStringView(
    const QtPrivate::XmlStringRef *lhs,
    const QString *rhs) {
  return operator<(*lhs, QStringView(*rhs));
}

//  bool operator<(QStringView lhs, const XmlStringRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateltE11QStringViewRKNS_12XmlStringRefE(
    const QString *lhs,
    const QtPrivate::XmlStringRef *rhs) {
  return operator<(QStringView(*lhs), *rhs);
}

//  bool operator>(const XmlStringRef &lhs, QStringView rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivategtERKNS_12XmlStringRefE11QStringView(
    const QtPrivate::XmlStringRef *lhs,
    const QString *rhs) {
  return operator>(*lhs, QStringView(*rhs));
}

//  bool operator>(QStringView lhs, const XmlStringRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivategtE11QStringViewRKNS_12XmlStringRefE(
    const QString *lhs,
    const QtPrivate::XmlStringRef *rhs) {
  return operator>(QStringView(*lhs), *rhs);
}

//  void QtPrivate::XmlStringRef::verify(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QtPrivate12XmlStringRef6verifyExx(
    const QtPrivate::XmlStringRef *self,
    qsizetype pos,
    qsizetype n) {
  self->verify(pos, n);
}

//  QtPrivate::XmlStringRef::~XmlStringRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate12XmlStringRefD1Ev(QtPrivate::XmlStringRef *self) {
  delete self;
}

#endif  // QT_CONFIG(xmlstream)
