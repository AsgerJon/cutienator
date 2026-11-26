//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4string_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4string_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  void QV4::Heap::String::markObjects(Heap::Base *that, MarkStack
//      *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap6String11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *that,
    QV4::MarkStack *markStack) {
  QV4::Heap::String::markObjects(that, markStack);
}

//  const VTable *QV4::Heap::String::vtable() const
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZNK3QV44Heap6String6vtableEv(
    const QV4::Heap::String *self) {
  return self->vtable();
}

//  void QV4::Heap::String::init(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap6String4initERK7QString(
    QV4::Heap::String *self,
    const QString *text) {
  self->init(*text);
}

//  void QV4::Heap::String::simplifyString() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV44Heap6String14simplifyStringEv(
    const QV4::Heap::String *self) {
  self->simplifyString();
}

//  int QV4::Heap::String::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV44Heap6String6lengthEv(const QV4::Heap::String *self) {
  return self->length();
}

//  std::size_t QV4::Heap::String::retainedTextSize() const
extern "C" Q_DECL_EXPORT
std::size_t ritual_ZNK3QV44Heap6String16retainedTextSizeEv(
    const QV4::Heap::String *self) {
  return self->retainedTextSize();
}

//  QString QV4::Heap::String::toQString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV44Heap6String9toQStringEv(
    const QV4::Heap::String *self) {
  return new QString(self->toQString());
}

//  bool QV4::Heap::String::isEqualTo(const String *other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap6String9isEqualToEPKS1_(
    const QV4::Heap::String *self,
    const QV4::Heap::String *other) {
  return self->isEqualTo(other);
}

//  bool QV4::Heap::String::startsWithUpper() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap6String15startsWithUpperEv(
    const QV4::Heap::String *self) {
  return self->startsWithUpper();
}

//  void QV4::Heap::String::append(const String *data, QChar *ch)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap6String6appendEPKS1_P5QChar(
    const QV4::Heap::String *data,
    QChar *ch) {
  QV4::Heap::String::append(data, ch);
}
