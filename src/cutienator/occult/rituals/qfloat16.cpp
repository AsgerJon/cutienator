//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfloat16.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/QtCore>
#include <QtCore/qtestsupport_core.h>
#include <QtCore/qtmochelpers.h>

//  qfloat16::qfloat16(Qt::Initialization a0)
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_ZN8qfloat16C1EN2Qt14InitializationE(Qt::Initialization a0) {
  return new qfloat16(a0);
}

//  qfloat16::qfloat16()
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_ZN8qfloat16C1Ev() {
  return new qfloat16();
}

//  qfloat16::qfloat16(float f)
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_ZN8qfloat16C1Ef(float f) {
  return new qfloat16(f);
}

//  float qfloat16::operator float() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8qfloat16cvfEv(const qfloat16 *self) {
  return self->operator float();
}

//  bool qfloat16::isInf() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8qfloat165isInfEv(const qfloat16 *self) {
  return self->isInf();
}

//  bool qfloat16::isNaN() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8qfloat165isNaNEv(const qfloat16 *self) {
  return self->isNaN();
}

//  bool qfloat16::isFinite() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8qfloat168isFiniteEv(const qfloat16 *self) {
  return self->isFinite();
}

//  int qfloat16::fpClassify() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8qfloat1610fpClassifyEv(const qfloat16 *self) {
  return self->fpClassify();
}

//  qfloat16 qfloat16::copySign(qfloat16 sign) const
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_ZNK8qfloat168copySignES_(
    const qfloat16 *self,
    const qfloat16 *sign) {
  return new qfloat16(self->copySign(*sign));
}

//  qfloat16 qfloat16::_limit_epsilon()
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_ZN8qfloat1614_limit_epsilonEv() {
  return new qfloat16(qfloat16::_limit_epsilon());
}

//  qfloat16 qfloat16::_limit_min()
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_ZN8qfloat1610_limit_minEv() {
  return new qfloat16(qfloat16::_limit_min());
}

//  qfloat16 qfloat16::_limit_denorm_min()
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_ZN8qfloat1617_limit_denorm_minEv() {
  return new qfloat16(qfloat16::_limit_denorm_min());
}

//  qfloat16 qfloat16::_limit_max()
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_ZN8qfloat1610_limit_maxEv() {
  return new qfloat16(qfloat16::_limit_max());
}

//  qfloat16 qfloat16::_limit_lowest()
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_ZN8qfloat1613_limit_lowestEv() {
  return new qfloat16(qfloat16::_limit_lowest());
}

//  qfloat16 qfloat16::_limit_infinity()
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_ZN8qfloat1615_limit_infinityEv() {
  return new qfloat16(qfloat16::_limit_infinity());
}

//  qfloat16 qfloat16::_limit_quiet_NaN()
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_ZN8qfloat1616_limit_quiet_NaNEv() {
  return new qfloat16(qfloat16::_limit_quiet_NaN());
}

//  qfloat16 qfloat16::_limit_signaling_NaN()
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_ZN8qfloat1620_limit_signaling_NaNEv() {
  return new qfloat16(qfloat16::_limit_signaling_NaN());
}

//  bool qfloat16::isNormal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8qfloat168isNormalEv(const qfloat16 *self) {
  return self->isNormal();
}

//  qfloat16 qfloat16::operator++(int a0)
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_ZN8qfloat16ppEi(qfloat16 *self, int a0) {
  return new qfloat16(self->operator++(a0));
}

//  qfloat16 qfloat16::operator--(int a0)
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_ZN8qfloat16mmEi(qfloat16 *self, int a0) {
  return new qfloat16(self->operator--(a0));
}

//  qfloat16::~qfloat16()
extern "C" Q_DECL_EXPORT
void ritual_ZN8qfloat16D1Ev(qfloat16 *self) {
  delete self;
}
