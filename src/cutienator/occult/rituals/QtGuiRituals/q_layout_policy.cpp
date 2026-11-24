//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qlayoutpolicy_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qlayoutpolicy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QLayoutPolicy::QLayoutPolicy()
extern "C" Q_DECL_EXPORT
QLayoutPolicy *ritual_ZN13QLayoutPolicyC1Ev() {
  return new QLayoutPolicy();
}

//  QLayoutPolicy::QLayoutPolicy(Policy horizontal, Policy vertical,
//      ControlType type)
extern "C" Q_DECL_EXPORT
QLayoutPolicy *ritual_ZN13QLayoutPolicyC1E6QFlagsINS_10PolicyFlagEES2_NS_11ControlTypeE(
    int horizontal,
    int vertical,
    QLayoutPolicy::ControlType type) {
  return new QLayoutPolicy(
      QFlags<QLayoutPolicy::PolicyFlag>::fromInt(horizontal),
      QFlags<QLayoutPolicy::PolicyFlag>::fromInt(vertical),
      type);
}

//  Policy QLayoutPolicy::horizontalPolicy() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLayoutPolicy16horizontalPolicyEv(
    const QLayoutPolicy *self) {
  return static_cast<int>(self->horizontalPolicy().toInt());
}

//  Policy QLayoutPolicy::verticalPolicy() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLayoutPolicy14verticalPolicyEv(const QLayoutPolicy *self) {
  return static_cast<int>(self->verticalPolicy().toInt());
}

//  ControlType QLayoutPolicy::controlType() const
extern "C" Q_DECL_EXPORT
QLayoutPolicy::ControlType ritual_ZNK13QLayoutPolicy11controlTypeEv(
    const QLayoutPolicy *self) {
  return self->controlType();
}

//  void QLayoutPolicy::setHorizontalPolicy(Policy d)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutPolicy19setHorizontalPolicyE6QFlagsINS_10PolicyFlagEE(
    QLayoutPolicy *self,
    int d) {
  self->setHorizontalPolicy(QFlags<QLayoutPolicy::PolicyFlag>::fromInt(d));
}

//  void QLayoutPolicy::setVerticalPolicy(Policy d)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutPolicy17setVerticalPolicyE6QFlagsINS_10PolicyFlagEE(
    QLayoutPolicy *self,
    int d) {
  self->setVerticalPolicy(QFlags<QLayoutPolicy::PolicyFlag>::fromInt(d));
}

//  void QLayoutPolicy::setControlType(ControlType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutPolicy14setControlTypeENS_11ControlTypeE(
    QLayoutPolicy *self,
    QLayoutPolicy::ControlType type) {
  self->setControlType(type);
}

//  Qt::Orientations QLayoutPolicy::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLayoutPolicy19expandingDirectionsEv(
    const QLayoutPolicy *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  void QLayoutPolicy::setHeightForWidth(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutPolicy17setHeightForWidthEb(
    QLayoutPolicy *self,
    bool b) {
  self->setHeightForWidth(b);
}

//  bool QLayoutPolicy::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLayoutPolicy17hasHeightForWidthEv(
    const QLayoutPolicy *self) {
  return self->hasHeightForWidth();
}

//  void QLayoutPolicy::setWidthForHeight(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutPolicy17setWidthForHeightEb(
    QLayoutPolicy *self,
    bool b) {
  self->setWidthForHeight(b);
}

//  bool QLayoutPolicy::hasWidthForHeight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLayoutPolicy17hasWidthForHeightEv(
    const QLayoutPolicy *self) {
  return self->hasWidthForHeight();
}

//  bool QLayoutPolicy::operator==(const QLayoutPolicy &s) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLayoutPolicyeqERKS_(
    const QLayoutPolicy *self,
    const QLayoutPolicy *s) {
  return self->operator==(*s);
}

//  bool QLayoutPolicy::operator!=(const QLayoutPolicy &s) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLayoutPolicyneERKS_(
    const QLayoutPolicy *self,
    const QLayoutPolicy *s) {
  return self->operator!=(*s);
}

//  int QLayoutPolicy::horizontalStretch() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLayoutPolicy17horizontalStretchEv(
    const QLayoutPolicy *self) {
  return self->horizontalStretch();
}

//  int QLayoutPolicy::verticalStretch() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLayoutPolicy15verticalStretchEv(const QLayoutPolicy *self) {
  return self->verticalStretch();
}

//  void QLayoutPolicy::setHorizontalStretch(int stretchFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutPolicy20setHorizontalStretchEi(
    QLayoutPolicy *self,
    int stretchFactor) {
  self->setHorizontalStretch(stretchFactor);
}

//  void QLayoutPolicy::setVerticalStretch(int stretchFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutPolicy18setVerticalStretchEi(
    QLayoutPolicy *self,
    int stretchFactor) {
  self->setVerticalStretch(stretchFactor);
}

//  void QLayoutPolicy::transpose()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutPolicy9transposeEv(QLayoutPolicy *self) {
  self->transpose();
}

//  QLayoutPolicy::QLayoutPolicy(int i)
extern "C" Q_DECL_EXPORT
QLayoutPolicy *ritual_ZN13QLayoutPolicyC1Ei(int i) {
  return new QLayoutPolicy(i);
}

//  QLayoutPolicy::~QLayoutPolicy()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutPolicyD1Ev(QLayoutPolicy *self) {
  delete self;
}
