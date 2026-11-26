//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/inlinecomponentutils_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/inlinecomponentutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  icutils::Node::Node()
extern "C" Q_DECL_EXPORT
icutils::Node *ritual_ZN7icutils4NodeC1Ev() {
  return new icutils::Node();
}

//  icutils::Node::Node(const Node &a0)
extern "C" Q_DECL_EXPORT
icutils::Node *ritual_ZN7icutils4NodeC1ERKS0_(const icutils::Node *a0) {
  return new icutils::Node(*a0);
}

//  icutils::Node::Node(Node &&a0)
extern "C" Q_DECL_EXPORT
icutils::Node *ritual_ZN7icutils4NodeC1EOS0_(icutils::Node *a0) {
  return new icutils::Node(std::move(*a0));
}

//  Node &icutils::Node::operator=(const Node &a0)
extern "C" Q_DECL_EXPORT
icutils::Node *ritual_ZN7icutils4NodeaSERKS0_(
    icutils::Node *self,
    const icutils::Node *a0) {
  return &(self->operator=(*a0));
}

//  Node &icutils::Node::operator=(Node &&a0)
extern "C" Q_DECL_EXPORT
icutils::Node *ritual_ZN7icutils4NodeaSEOS0_(
    icutils::Node *self,
    icutils::Node *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  bool icutils::Node::operator==(const Node &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7icutils4NodeeqERKS0_(
    const icutils::Node *self,
    const icutils::Node *other) {
  return self->operator==(*other);
}

//  icutils::Node::Node(IndexType s)
extern "C" Q_DECL_EXPORT
icutils::Node *ritual_ZN7icutils4NodeC1Em(unsigned long long s) {
  return new icutils::Node(s);
}

//  bool icutils::Node::hasPermanentMark() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7icutils4Node16hasPermanentMarkEv(const icutils::Node *self) {
  return self->hasPermanentMark();
}

//  bool icutils::Node::hasTemporaryMark() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7icutils4Node16hasTemporaryMarkEv(const icutils::Node *self) {
  return self->hasTemporaryMark();
}

//  void icutils::Node::setPermanentMark()
extern "C" Q_DECL_EXPORT
void ritual_ZN7icutils4Node16setPermanentMarkEv(icutils::Node *self) {
  self->setPermanentMark();
}

//  void icutils::Node::setTemporaryMark()
extern "C" Q_DECL_EXPORT
void ritual_ZN7icutils4Node16setTemporaryMarkEv(icutils::Node *self) {
  self->setTemporaryMark();
}

//  IndexType icutils::Node::index() const
extern "C" Q_DECL_EXPORT
unsigned long long ritual_ZNK7icutils4Node5indexEv(
    const icutils::Node *self) {
  return self->index();
}

//  icutils::Node::~Node()
extern "C" Q_DECL_EXPORT
void ritual_ZN7icutils4NodeD1Ev(icutils::Node *self) {
  delete self;
}
