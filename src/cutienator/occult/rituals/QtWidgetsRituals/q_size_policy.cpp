//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qsizepolicy.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qsizepolicy.h>
#include <QtCore/qvariant.h>
#include <QtWidgets/QSizePolicy>

//  QSizePolicy::QSizePolicy()
extern "C" Q_DECL_EXPORT
QSizePolicy *ritual_ZN11QSizePolicyC1Ev() {
  return new QSizePolicy();
}

//  QSizePolicy::QSizePolicy(Policy horizontal, Policy vertical, ControlType
//      type)
extern "C" Q_DECL_EXPORT
QSizePolicy *ritual_ZN11QSizePolicyC1ENS_6PolicyES0_NS_11ControlTypeE(
    QSizePolicy::Policy horizontal,
    QSizePolicy::Policy vertical,
    QSizePolicy::ControlType type) {
  return new QSizePolicy(horizontal, vertical, type);
}

//  Policy QSizePolicy::horizontalPolicy() const
extern "C" Q_DECL_EXPORT
QSizePolicy::Policy ritual_ZNK11QSizePolicy16horizontalPolicyEv(
    const QSizePolicy *self) {
  return self->horizontalPolicy();
}

//  Policy QSizePolicy::verticalPolicy() const
extern "C" Q_DECL_EXPORT
QSizePolicy::Policy ritual_ZNK11QSizePolicy14verticalPolicyEv(
    const QSizePolicy *self) {
  return self->verticalPolicy();
}

//  ControlType QSizePolicy::controlType() const
extern "C" Q_DECL_EXPORT
QSizePolicy::ControlType ritual_ZNK11QSizePolicy11controlTypeEv(
    const QSizePolicy *self) {
  return self->controlType();
}

//  void QSizePolicy::setHorizontalPolicy(Policy d)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSizePolicy19setHorizontalPolicyENS_6PolicyE(
    QSizePolicy *self,
    QSizePolicy::Policy d) {
  self->setHorizontalPolicy(d);
}

//  void QSizePolicy::setVerticalPolicy(Policy d)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSizePolicy17setVerticalPolicyENS_6PolicyE(
    QSizePolicy *self,
    QSizePolicy::Policy d) {
  self->setVerticalPolicy(d);
}

//  void QSizePolicy::setControlType(ControlType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSizePolicy14setControlTypeENS_11ControlTypeE(
    QSizePolicy *self,
    QSizePolicy::ControlType type) {
  self->setControlType(type);
}

//  Qt::Orientations QSizePolicy::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSizePolicy19expandingDirectionsEv(const QSizePolicy *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  void QSizePolicy::setHeightForWidth(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSizePolicy17setHeightForWidthEb(QSizePolicy *self, bool b) {
  self->setHeightForWidth(b);
}

//  bool QSizePolicy::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSizePolicy17hasHeightForWidthEv(const QSizePolicy *self) {
  return self->hasHeightForWidth();
}

//  void QSizePolicy::setWidthForHeight(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSizePolicy17setWidthForHeightEb(QSizePolicy *self, bool b) {
  self->setWidthForHeight(b);
}

//  bool QSizePolicy::hasWidthForHeight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSizePolicy17hasWidthForHeightEv(const QSizePolicy *self) {
  return self->hasWidthForHeight();
}

//  bool QSizePolicy::operator==(const QSizePolicy &s) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSizePolicyeqERKS_(
    const QSizePolicy *self,
    const QSizePolicy *s) {
  return self->operator==(*s);
}

//  bool QSizePolicy::operator!=(const QSizePolicy &s) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSizePolicyneERKS_(
    const QSizePolicy *self,
    const QSizePolicy *s) {
  return self->operator!=(*s);
}

//  QVariant QSizePolicy::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QSizePolicycv8QVariantEv(const QSizePolicy *self) {
  return new QVariant(self->operator QVariant());
}

//  int QSizePolicy::horizontalStretch() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSizePolicy17horizontalStretchEv(const QSizePolicy *self) {
  return self->horizontalStretch();
}

//  int QSizePolicy::verticalStretch() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSizePolicy15verticalStretchEv(const QSizePolicy *self) {
  return self->verticalStretch();
}

//  void QSizePolicy::setHorizontalStretch(int stretchFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSizePolicy20setHorizontalStretchEi(
    QSizePolicy *self,
    int stretchFactor) {
  self->setHorizontalStretch(stretchFactor);
}

//  void QSizePolicy::setVerticalStretch(int stretchFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSizePolicy18setVerticalStretchEi(
    QSizePolicy *self,
    int stretchFactor) {
  self->setVerticalStretch(stretchFactor);
}

//  bool QSizePolicy::retainSizeWhenHidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSizePolicy20retainSizeWhenHiddenEv(
    const QSizePolicy *self) {
  return self->retainSizeWhenHidden();
}

//  void QSizePolicy::setRetainSizeWhenHidden(bool retainSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSizePolicy23setRetainSizeWhenHiddenEb(
    QSizePolicy *self,
    bool retainSize) {
  self->setRetainSizeWhenHidden(retainSize);
}

//  void QSizePolicy::transpose()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSizePolicy9transposeEv(QSizePolicy *self) {
  self->transpose();
}

//  QSizePolicy QSizePolicy::transposed() const
extern "C" Q_DECL_EXPORT
QSizePolicy *ritual_ZNK11QSizePolicy10transposedEv(const QSizePolicy *self) {
  return new QSizePolicy(self->transposed());
}

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator<<(QDataStream &a0, const QSizePolicy &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK11QSizePolicy(
    QDataStream *a0,
    const QSizePolicy *a1) {
  return &(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator>>(QDataStream &a0, QSizePolicy &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR11QSizePolicy(
    QDataStream *a0,
    QSizePolicy *a1) {
  return &(operator>>(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

//  QSizePolicy::QSizePolicy(int i)
extern "C" Q_DECL_EXPORT
QSizePolicy *ritual_ZN11QSizePolicyC1Ei(int i) {
  return new QSizePolicy(i);
}

//  QSizePolicy::QSizePolicy(Bits b)
extern "C" Q_DECL_EXPORT
QSizePolicy *ritual_ZN11QSizePolicyC1ENS_4BitsE(const QSizePolicy::Bits *b) {
  return new QSizePolicy(*b);
}

//  quint32 QSizePolicy::toControlTypeFieldValue(ControlType type)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN11QSizePolicy23toControlTypeFieldValueENS_11ControlTypeE(
    QSizePolicy::ControlType type) {
  return QSizePolicy::toControlTypeFieldValue(type);
}

//  QSizePolicy::~QSizePolicy()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSizePolicyD1Ev(QSizePolicy *self) {
  delete self;
}
