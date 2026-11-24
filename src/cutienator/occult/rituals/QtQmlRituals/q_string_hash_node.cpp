//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qstringhash_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qstringhash_p.h>
#include <QtQml/6.12.0/QtQml/private/qhashedstring_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QStringHashNode::QStringHashNode()
extern "C" Q_DECL_EXPORT
QStringHashNode *ritual_ZN15QStringHashNodeC1Ev() {
  return new QStringHashNode();
}

//  QStringHashNode::QStringHashNode(const QHashedString &key)
extern "C" Q_DECL_EXPORT
QStringHashNode *ritual_ZN15QStringHashNodeC1ERK13QHashedString(
    const QHashedString *key) {
  return new QStringHashNode(*key);
}

//  QStringHashNode::QStringHashNode(const QHashedCStringRef &key)
extern "C" Q_DECL_EXPORT
QStringHashNode *ritual_ZN15QStringHashNodeC1ERK17QHashedCStringRef(
    const QHashedCStringRef *key) {
  return new QStringHashNode(*key);
}

//  QStringHashNode::QStringHashNode(const QStringHashNode &o)
extern "C" Q_DECL_EXPORT
QStringHashNode *ritual_ZN15QStringHashNodeC1ERKS_(
    const QStringHashNode *o) {
  return new QStringHashNode(*o);
}

//  QStringHashNode::~QStringHashNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStringHashNodeD1Ev(QStringHashNode *self) {
  delete self;
}

//  QHashedString QStringHashNode::key() const
extern "C" Q_DECL_EXPORT
QHashedString *ritual_ZNK15QStringHashNode3keyEv(
    const QStringHashNode *self) {
  return new QHashedString(self->key());
}

//  bool QStringHashNode::isQString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QStringHashNode9isQStringEv(const QStringHashNode *self) {
  return self->isQString();
}

//  void QStringHashNode::setQString(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStringHashNode10setQStringEb(
    QStringHashNode *self,
    bool v) {
  self->setQString(v);
}

//  qsizetype QStringHashNode::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK15QStringHashNode4sizeEv(const QStringHashNode *self) {
  return self->size();
}

//  const char *QStringHashNode::cStrData() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK15QStringHashNode8cStrDataEv(
    const QStringHashNode *self) {
  return self->cStrData();
}

//  bool QStringHashNode::equals(const QV4::Value &string) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QStringHashNode6equalsERKN3QV45ValueE(
    const QStringHashNode *self,
    const QV4::Value *string) {
  return self->equals(*string);
}

//  bool QStringHashNode::equals(const QV4::String *string) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QStringHashNode6equalsEPKN3QV46StringE(
    const QStringHashNode *self,
    const QV4::String *string) {
  return self->equals(string);
}

//  bool QStringHashNode::equals(const QHashedStringRef &string) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QStringHashNode6equalsERK16QHashedStringRef(
    const QStringHashNode *self,
    const QHashedStringRef *string) {
  return self->equals(*string);
}

//  bool QStringHashNode::equals(const QHashedCStringRef &string) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QStringHashNode6equalsERK17QHashedCStringRef(
    const QStringHashNode *self,
    const QHashedCStringRef *string) {
  return self->equals(*string);
}
