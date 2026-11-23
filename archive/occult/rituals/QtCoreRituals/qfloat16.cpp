//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfloat16.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetatype.h>

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

//  qfloat16 operator+(qfloat16 a)
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_Zps8qfloat16(const qfloat16 *a) {
  return new qfloat16(operator+(*a));
}

//  qfloat16 operator-(qfloat16 a)
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_Zng8qfloat16(const qfloat16 *a) {
  return new qfloat16(operator-(*a));
}

//  qfloat16 operator+(qfloat16 a, qfloat16 b)
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_Zpl8qfloat16S_(const qfloat16 *a, const qfloat16 *b) {
  return new qfloat16(operator+(*a, *b));
}

//  qfloat16 operator-(qfloat16 a, qfloat16 b)
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_Zmi8qfloat16S_(const qfloat16 *a, const qfloat16 *b) {
  return new qfloat16(operator-(*a, *b));
}

//  qfloat16 operator*(qfloat16 a, qfloat16 b)
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_Zml8qfloat16S_(const qfloat16 *a, const qfloat16 *b) {
  return new qfloat16(operator*(*a, *b));
}

//  qfloat16 operator/(qfloat16 a, qfloat16 b)
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_Zdv8qfloat16S_(const qfloat16 *a, const qfloat16 *b) {
  return new qfloat16(operator/(*a, *b));
}

//  double operator+(qfloat16 lhs, double rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zpl8qfloat16d(const qfloat16 *lhs, double rhs) {
  return operator+(*lhs, rhs);
}

//  double operator+(double lhs, qfloat16 rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zpld8qfloat16(double lhs, const qfloat16 *rhs) {
  return operator+(lhs, *rhs);
}

//  double operator-(qfloat16 lhs, double rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zmi8qfloat16d(const qfloat16 *lhs, double rhs) {
  return operator-(*lhs, rhs);
}

//  double operator-(double lhs, qfloat16 rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zmid8qfloat16(double lhs, const qfloat16 *rhs) {
  return operator-(lhs, *rhs);
}

//  double operator*(qfloat16 lhs, double rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zml8qfloat16d(const qfloat16 *lhs, double rhs) {
  return operator*(*lhs, rhs);
}

//  double operator*(double lhs, qfloat16 rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zmld8qfloat16(double lhs, const qfloat16 *rhs) {
  return operator*(lhs, *rhs);
}

//  double operator/(qfloat16 lhs, double rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zdv8qfloat16d(const qfloat16 *lhs, double rhs) {
  return operator/(*lhs, rhs);
}

//  double operator/(double lhs, qfloat16 rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zdvd8qfloat16(double lhs, const qfloat16 *rhs) {
  return operator/(lhs, *rhs);
}

//  float operator+(qfloat16 lhs, float rhs)
extern "C" Q_DECL_EXPORT
float ritual_Zpl8qfloat16f(const qfloat16 *lhs, float rhs) {
  return operator+(*lhs, rhs);
}

//  float operator+(float lhs, qfloat16 rhs)
extern "C" Q_DECL_EXPORT
float ritual_Zplf8qfloat16(float lhs, const qfloat16 *rhs) {
  return operator+(lhs, *rhs);
}

//  float operator-(qfloat16 lhs, float rhs)
extern "C" Q_DECL_EXPORT
float ritual_Zmi8qfloat16f(const qfloat16 *lhs, float rhs) {
  return operator-(*lhs, rhs);
}

//  float operator-(float lhs, qfloat16 rhs)
extern "C" Q_DECL_EXPORT
float ritual_Zmif8qfloat16(float lhs, const qfloat16 *rhs) {
  return operator-(lhs, *rhs);
}

//  float operator*(qfloat16 lhs, float rhs)
extern "C" Q_DECL_EXPORT
float ritual_Zml8qfloat16f(const qfloat16 *lhs, float rhs) {
  return operator*(*lhs, rhs);
}

//  float operator*(float lhs, qfloat16 rhs)
extern "C" Q_DECL_EXPORT
float ritual_Zmlf8qfloat16(float lhs, const qfloat16 *rhs) {
  return operator*(lhs, *rhs);
}

//  float operator/(qfloat16 lhs, float rhs)
extern "C" Q_DECL_EXPORT
float ritual_Zdv8qfloat16f(const qfloat16 *lhs, float rhs) {
  return operator/(*lhs, rhs);
}

//  float operator/(float lhs, qfloat16 rhs)
extern "C" Q_DECL_EXPORT
float ritual_Zdvf8qfloat16(float lhs, const qfloat16 *rhs) {
  return operator/(lhs, *rhs);
}

//  double operator+(qfloat16 lhs, int rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zpl8qfloat16i(const qfloat16 *lhs, int rhs) {
  return operator+(*lhs, rhs);
}

//  double operator+(int lhs, qfloat16 rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zpli8qfloat16(int lhs, const qfloat16 *rhs) {
  return operator+(lhs, *rhs);
}

//  double operator-(qfloat16 lhs, int rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zmi8qfloat16i(const qfloat16 *lhs, int rhs) {
  return operator-(*lhs, rhs);
}

//  double operator-(int lhs, qfloat16 rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zmii8qfloat16(int lhs, const qfloat16 *rhs) {
  return operator-(lhs, *rhs);
}

//  double operator*(qfloat16 lhs, int rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zml8qfloat16i(const qfloat16 *lhs, int rhs) {
  return operator*(*lhs, rhs);
}

//  double operator*(int lhs, qfloat16 rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zmli8qfloat16(int lhs, const qfloat16 *rhs) {
  return operator*(lhs, *rhs);
}

//  double operator/(qfloat16 lhs, int rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zdv8qfloat16i(const qfloat16 *lhs, int rhs) {
  return operator/(*lhs, rhs);
}

//  double operator/(int lhs, qfloat16 rhs)
extern "C" Q_DECL_EXPORT
double ritual_Zdvi8qfloat16(int lhs, const qfloat16 *rhs) {
  return operator/(lhs, *rhs);
}

//  bool operator==(const qfloat16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8qfloat16S1_(const qfloat16 *lhs, const qfloat16 *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const qfloat16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8qfloat16S1_(const qfloat16 *lhs, const qfloat16 *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const qfloat16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8qfloat16S1_(const qfloat16 *lhs, const qfloat16 *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const qfloat16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8qfloat16S1_(const qfloat16 *lhs, const qfloat16 *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const qfloat16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8qfloat16S1_(const qfloat16 *lhs, const qfloat16 *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const qfloat16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8qfloat16S1_(const qfloat16 *lhs, const qfloat16 *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const qfloat16 &lhs, const double &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8qfloat16RKd(const qfloat16 *lhs, double rhs) {
  return operator==(*lhs, rhs);
}

//  bool operator!=(const qfloat16 &lhs, const double &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8qfloat16RKd(const qfloat16 *lhs, double rhs) {
  return operator!=(*lhs, rhs);
}

//  bool operator<(const qfloat16 &lhs, const double &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8qfloat16RKd(const qfloat16 *lhs, double rhs) {
  return operator<(*lhs, rhs);
}

//  bool operator>(const qfloat16 &lhs, const double &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8qfloat16RKd(const qfloat16 *lhs, double rhs) {
  return operator>(*lhs, rhs);
}

//  bool operator<=(const qfloat16 &lhs, const double &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8qfloat16RKd(const qfloat16 *lhs, double rhs) {
  return operator<=(*lhs, rhs);
}

//  bool operator>=(const qfloat16 &lhs, const double &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8qfloat16RKd(const qfloat16 *lhs, double rhs) {
  return operator>=(*lhs, rhs);
}

//  bool operator==(const double &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKdRK8qfloat16(double lhs, const qfloat16 *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(const double &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKdRK8qfloat16(double lhs, const qfloat16 *rhs) {
  return operator!=(lhs, *rhs);
}

//  bool operator<(const double &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKdRK8qfloat16(double lhs, const qfloat16 *rhs) {
  return operator<(lhs, *rhs);
}

//  bool operator>(const double &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKdRK8qfloat16(double lhs, const qfloat16 *rhs) {
  return operator>(lhs, *rhs);
}

//  bool operator<=(const double &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKdRK8qfloat16(double lhs, const qfloat16 *rhs) {
  return operator<=(lhs, *rhs);
}

//  bool operator>=(const double &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKdRK8qfloat16(double lhs, const qfloat16 *rhs) {
  return operator>=(lhs, *rhs);
}

//  bool operator==(const qfloat16 &lhs, const float &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8qfloat16RKf(const qfloat16 *lhs, float rhs) {
  return operator==(*lhs, rhs);
}

//  bool operator!=(const qfloat16 &lhs, const float &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8qfloat16RKf(const qfloat16 *lhs, float rhs) {
  return operator!=(*lhs, rhs);
}

//  bool operator<(const qfloat16 &lhs, const float &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8qfloat16RKf(const qfloat16 *lhs, float rhs) {
  return operator<(*lhs, rhs);
}

//  bool operator>(const qfloat16 &lhs, const float &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8qfloat16RKf(const qfloat16 *lhs, float rhs) {
  return operator>(*lhs, rhs);
}

//  bool operator<=(const qfloat16 &lhs, const float &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8qfloat16RKf(const qfloat16 *lhs, float rhs) {
  return operator<=(*lhs, rhs);
}

//  bool operator>=(const qfloat16 &lhs, const float &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8qfloat16RKf(const qfloat16 *lhs, float rhs) {
  return operator>=(*lhs, rhs);
}

//  bool operator==(const float &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKfRK8qfloat16(float lhs, const qfloat16 *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(const float &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKfRK8qfloat16(float lhs, const qfloat16 *rhs) {
  return operator!=(lhs, *rhs);
}

//  bool operator<(const float &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKfRK8qfloat16(float lhs, const qfloat16 *rhs) {
  return operator<(lhs, *rhs);
}

//  bool operator>(const float &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKfRK8qfloat16(float lhs, const qfloat16 *rhs) {
  return operator>(lhs, *rhs);
}

//  bool operator<=(const float &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKfRK8qfloat16(float lhs, const qfloat16 *rhs) {
  return operator<=(lhs, *rhs);
}

//  bool operator>=(const float &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKfRK8qfloat16(float lhs, const qfloat16 *rhs) {
  return operator>=(lhs, *rhs);
}

//  bool operator==(const qfloat16 &lhs, const qint8 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8qfloat16RKa(const qfloat16 *lhs, qint8 rhs) {
  return operator==(*lhs, rhs);
}

//  bool operator!=(const qfloat16 &lhs, const qint8 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8qfloat16RKa(const qfloat16 *lhs, qint8 rhs) {
  return operator!=(*lhs, rhs);
}

//  bool operator<(const qfloat16 &lhs, const qint8 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8qfloat16RKa(const qfloat16 *lhs, qint8 rhs) {
  return operator<(*lhs, rhs);
}

//  bool operator>(const qfloat16 &lhs, const qint8 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8qfloat16RKa(const qfloat16 *lhs, qint8 rhs) {
  return operator>(*lhs, rhs);
}

//  bool operator<=(const qfloat16 &lhs, const qint8 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8qfloat16RKa(const qfloat16 *lhs, qint8 rhs) {
  return operator<=(*lhs, rhs);
}

//  bool operator>=(const qfloat16 &lhs, const qint8 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8qfloat16RKa(const qfloat16 *lhs, qint8 rhs) {
  return operator>=(*lhs, rhs);
}

//  bool operator==(const qint8 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKaRK8qfloat16(qint8 lhs, const qfloat16 *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(const qint8 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKaRK8qfloat16(qint8 lhs, const qfloat16 *rhs) {
  return operator!=(lhs, *rhs);
}

//  bool operator<(const qint8 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKaRK8qfloat16(qint8 lhs, const qfloat16 *rhs) {
  return operator<(lhs, *rhs);
}

//  bool operator>(const qint8 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKaRK8qfloat16(qint8 lhs, const qfloat16 *rhs) {
  return operator>(lhs, *rhs);
}

//  bool operator<=(const qint8 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKaRK8qfloat16(qint8 lhs, const qfloat16 *rhs) {
  return operator<=(lhs, *rhs);
}

//  bool operator>=(const qint8 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKaRK8qfloat16(qint8 lhs, const qfloat16 *rhs) {
  return operator>=(lhs, *rhs);
}

//  bool operator==(const qfloat16 &lhs, const quint8 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8qfloat16RKh(const qfloat16 *lhs, quint8 rhs) {
  return operator==(*lhs, rhs);
}

//  bool operator!=(const qfloat16 &lhs, const quint8 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8qfloat16RKh(const qfloat16 *lhs, quint8 rhs) {
  return operator!=(*lhs, rhs);
}

//  bool operator<(const qfloat16 &lhs, const quint8 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8qfloat16RKh(const qfloat16 *lhs, quint8 rhs) {
  return operator<(*lhs, rhs);
}

//  bool operator>(const qfloat16 &lhs, const quint8 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8qfloat16RKh(const qfloat16 *lhs, quint8 rhs) {
  return operator>(*lhs, rhs);
}

//  bool operator<=(const qfloat16 &lhs, const quint8 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8qfloat16RKh(const qfloat16 *lhs, quint8 rhs) {
  return operator<=(*lhs, rhs);
}

//  bool operator>=(const qfloat16 &lhs, const quint8 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8qfloat16RKh(const qfloat16 *lhs, quint8 rhs) {
  return operator>=(*lhs, rhs);
}

//  bool operator==(const quint8 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKhRK8qfloat16(quint8 lhs, const qfloat16 *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(const quint8 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKhRK8qfloat16(quint8 lhs, const qfloat16 *rhs) {
  return operator!=(lhs, *rhs);
}

//  bool operator<(const quint8 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKhRK8qfloat16(quint8 lhs, const qfloat16 *rhs) {
  return operator<(lhs, *rhs);
}

//  bool operator>(const quint8 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKhRK8qfloat16(quint8 lhs, const qfloat16 *rhs) {
  return operator>(lhs, *rhs);
}

//  bool operator<=(const quint8 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKhRK8qfloat16(quint8 lhs, const qfloat16 *rhs) {
  return operator<=(lhs, *rhs);
}

//  bool operator>=(const quint8 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKhRK8qfloat16(quint8 lhs, const qfloat16 *rhs) {
  return operator>=(lhs, *rhs);
}

//  bool operator==(const qfloat16 &lhs, const qint16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8qfloat16RKs(const qfloat16 *lhs, qint16 rhs) {
  return operator==(*lhs, rhs);
}

//  bool operator!=(const qfloat16 &lhs, const qint16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8qfloat16RKs(const qfloat16 *lhs, qint16 rhs) {
  return operator!=(*lhs, rhs);
}

//  bool operator<(const qfloat16 &lhs, const qint16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8qfloat16RKs(const qfloat16 *lhs, qint16 rhs) {
  return operator<(*lhs, rhs);
}

//  bool operator>(const qfloat16 &lhs, const qint16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8qfloat16RKs(const qfloat16 *lhs, qint16 rhs) {
  return operator>(*lhs, rhs);
}

//  bool operator<=(const qfloat16 &lhs, const qint16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8qfloat16RKs(const qfloat16 *lhs, qint16 rhs) {
  return operator<=(*lhs, rhs);
}

//  bool operator>=(const qfloat16 &lhs, const qint16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8qfloat16RKs(const qfloat16 *lhs, qint16 rhs) {
  return operator>=(*lhs, rhs);
}

//  bool operator==(const qint16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKsRK8qfloat16(qint16 lhs, const qfloat16 *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(const qint16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKsRK8qfloat16(qint16 lhs, const qfloat16 *rhs) {
  return operator!=(lhs, *rhs);
}

//  bool operator<(const qint16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKsRK8qfloat16(qint16 lhs, const qfloat16 *rhs) {
  return operator<(lhs, *rhs);
}

//  bool operator>(const qint16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKsRK8qfloat16(qint16 lhs, const qfloat16 *rhs) {
  return operator>(lhs, *rhs);
}

//  bool operator<=(const qint16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKsRK8qfloat16(qint16 lhs, const qfloat16 *rhs) {
  return operator<=(lhs, *rhs);
}

//  bool operator>=(const qint16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKsRK8qfloat16(qint16 lhs, const qfloat16 *rhs) {
  return operator>=(lhs, *rhs);
}

//  bool operator==(const qfloat16 &lhs, const quint16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8qfloat16RKt(const qfloat16 *lhs, quint16 rhs) {
  return operator==(*lhs, rhs);
}

//  bool operator!=(const qfloat16 &lhs, const quint16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8qfloat16RKt(const qfloat16 *lhs, quint16 rhs) {
  return operator!=(*lhs, rhs);
}

//  bool operator<(const qfloat16 &lhs, const quint16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8qfloat16RKt(const qfloat16 *lhs, quint16 rhs) {
  return operator<(*lhs, rhs);
}

//  bool operator>(const qfloat16 &lhs, const quint16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8qfloat16RKt(const qfloat16 *lhs, quint16 rhs) {
  return operator>(*lhs, rhs);
}

//  bool operator<=(const qfloat16 &lhs, const quint16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8qfloat16RKt(const qfloat16 *lhs, quint16 rhs) {
  return operator<=(*lhs, rhs);
}

//  bool operator>=(const qfloat16 &lhs, const quint16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8qfloat16RKt(const qfloat16 *lhs, quint16 rhs) {
  return operator>=(*lhs, rhs);
}

//  bool operator==(const quint16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKtRK8qfloat16(quint16 lhs, const qfloat16 *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(const quint16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKtRK8qfloat16(quint16 lhs, const qfloat16 *rhs) {
  return operator!=(lhs, *rhs);
}

//  bool operator<(const quint16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKtRK8qfloat16(quint16 lhs, const qfloat16 *rhs) {
  return operator<(lhs, *rhs);
}

//  bool operator>(const quint16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKtRK8qfloat16(quint16 lhs, const qfloat16 *rhs) {
  return operator>(lhs, *rhs);
}

//  bool operator<=(const quint16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKtRK8qfloat16(quint16 lhs, const qfloat16 *rhs) {
  return operator<=(lhs, *rhs);
}

//  bool operator>=(const quint16 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKtRK8qfloat16(quint16 lhs, const qfloat16 *rhs) {
  return operator>=(lhs, *rhs);
}

//  bool operator==(const qfloat16 &lhs, const qint32 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8qfloat16RKi(const qfloat16 *lhs, qint32 rhs) {
  return operator==(*lhs, rhs);
}

//  bool operator!=(const qfloat16 &lhs, const qint32 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8qfloat16RKi(const qfloat16 *lhs, qint32 rhs) {
  return operator!=(*lhs, rhs);
}

//  bool operator<(const qfloat16 &lhs, const qint32 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8qfloat16RKi(const qfloat16 *lhs, qint32 rhs) {
  return operator<(*lhs, rhs);
}

//  bool operator>(const qfloat16 &lhs, const qint32 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8qfloat16RKi(const qfloat16 *lhs, qint32 rhs) {
  return operator>(*lhs, rhs);
}

//  bool operator<=(const qfloat16 &lhs, const qint32 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8qfloat16RKi(const qfloat16 *lhs, qint32 rhs) {
  return operator<=(*lhs, rhs);
}

//  bool operator>=(const qfloat16 &lhs, const qint32 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8qfloat16RKi(const qfloat16 *lhs, qint32 rhs) {
  return operator>=(*lhs, rhs);
}

//  bool operator==(const qint32 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKiRK8qfloat16(qint32 lhs, const qfloat16 *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(const qint32 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKiRK8qfloat16(qint32 lhs, const qfloat16 *rhs) {
  return operator!=(lhs, *rhs);
}

//  bool operator<(const qint32 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKiRK8qfloat16(qint32 lhs, const qfloat16 *rhs) {
  return operator<(lhs, *rhs);
}

//  bool operator>(const qint32 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKiRK8qfloat16(qint32 lhs, const qfloat16 *rhs) {
  return operator>(lhs, *rhs);
}

//  bool operator<=(const qint32 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKiRK8qfloat16(qint32 lhs, const qfloat16 *rhs) {
  return operator<=(lhs, *rhs);
}

//  bool operator>=(const qint32 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKiRK8qfloat16(qint32 lhs, const qfloat16 *rhs) {
  return operator>=(lhs, *rhs);
}

//  bool operator==(const qfloat16 &lhs, const quint32 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8qfloat16RKj(const qfloat16 *lhs, quint32 rhs) {
  return operator==(*lhs, rhs);
}

//  bool operator!=(const qfloat16 &lhs, const quint32 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8qfloat16RKj(const qfloat16 *lhs, quint32 rhs) {
  return operator!=(*lhs, rhs);
}

//  bool operator<(const qfloat16 &lhs, const quint32 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8qfloat16RKj(const qfloat16 *lhs, quint32 rhs) {
  return operator<(*lhs, rhs);
}

//  bool operator>(const qfloat16 &lhs, const quint32 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8qfloat16RKj(const qfloat16 *lhs, quint32 rhs) {
  return operator>(*lhs, rhs);
}

//  bool operator<=(const qfloat16 &lhs, const quint32 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8qfloat16RKj(const qfloat16 *lhs, quint32 rhs) {
  return operator<=(*lhs, rhs);
}

//  bool operator>=(const qfloat16 &lhs, const quint32 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8qfloat16RKj(const qfloat16 *lhs, quint32 rhs) {
  return operator>=(*lhs, rhs);
}

//  bool operator==(const quint32 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKjRK8qfloat16(quint32 lhs, const qfloat16 *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(const quint32 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKjRK8qfloat16(quint32 lhs, const qfloat16 *rhs) {
  return operator!=(lhs, *rhs);
}

//  bool operator<(const quint32 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKjRK8qfloat16(quint32 lhs, const qfloat16 *rhs) {
  return operator<(lhs, *rhs);
}

//  bool operator>(const quint32 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKjRK8qfloat16(quint32 lhs, const qfloat16 *rhs) {
  return operator>(lhs, *rhs);
}

//  bool operator<=(const quint32 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKjRK8qfloat16(quint32 lhs, const qfloat16 *rhs) {
  return operator<=(lhs, *rhs);
}

//  bool operator>=(const quint32 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKjRK8qfloat16(quint32 lhs, const qfloat16 *rhs) {
  return operator>=(lhs, *rhs);
}

//  bool operator==(const qfloat16 &lhs, const long &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8qfloat16RKl(const qfloat16 *lhs, long rhs) {
  return operator==(*lhs, rhs);
}

//  bool operator!=(const qfloat16 &lhs, const long &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8qfloat16RKl(const qfloat16 *lhs, long rhs) {
  return operator!=(*lhs, rhs);
}

//  bool operator<(const qfloat16 &lhs, const long &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8qfloat16RKl(const qfloat16 *lhs, long rhs) {
  return operator<(*lhs, rhs);
}

//  bool operator>(const qfloat16 &lhs, const long &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8qfloat16RKl(const qfloat16 *lhs, long rhs) {
  return operator>(*lhs, rhs);
}

//  bool operator<=(const qfloat16 &lhs, const long &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8qfloat16RKl(const qfloat16 *lhs, long rhs) {
  return operator<=(*lhs, rhs);
}

//  bool operator>=(const qfloat16 &lhs, const long &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8qfloat16RKl(const qfloat16 *lhs, long rhs) {
  return operator>=(*lhs, rhs);
}

//  bool operator==(const long &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKlRK8qfloat16(long lhs, const qfloat16 *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(const long &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKlRK8qfloat16(long lhs, const qfloat16 *rhs) {
  return operator!=(lhs, *rhs);
}

//  bool operator<(const long &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKlRK8qfloat16(long lhs, const qfloat16 *rhs) {
  return operator<(lhs, *rhs);
}

//  bool operator>(const long &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKlRK8qfloat16(long lhs, const qfloat16 *rhs) {
  return operator>(lhs, *rhs);
}

//  bool operator<=(const long &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKlRK8qfloat16(long lhs, const qfloat16 *rhs) {
  return operator<=(lhs, *rhs);
}

//  bool operator>=(const long &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKlRK8qfloat16(long lhs, const qfloat16 *rhs) {
  return operator>=(lhs, *rhs);
}

//  bool operator==(const qfloat16 &lhs, const unsigned long &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8qfloat16RKm(const qfloat16 *lhs, unsigned long rhs) {
  return operator==(*lhs, rhs);
}

//  bool operator!=(const qfloat16 &lhs, const unsigned long &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8qfloat16RKm(const qfloat16 *lhs, unsigned long rhs) {
  return operator!=(*lhs, rhs);
}

//  bool operator<(const qfloat16 &lhs, const unsigned long &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8qfloat16RKm(const qfloat16 *lhs, unsigned long rhs) {
  return operator<(*lhs, rhs);
}

//  bool operator>(const qfloat16 &lhs, const unsigned long &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8qfloat16RKm(const qfloat16 *lhs, unsigned long rhs) {
  return operator>(*lhs, rhs);
}

//  bool operator<=(const qfloat16 &lhs, const unsigned long &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8qfloat16RKm(const qfloat16 *lhs, unsigned long rhs) {
  return operator<=(*lhs, rhs);
}

//  bool operator>=(const qfloat16 &lhs, const unsigned long &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8qfloat16RKm(const qfloat16 *lhs, unsigned long rhs) {
  return operator>=(*lhs, rhs);
}

//  bool operator==(const unsigned long &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKmRK8qfloat16(unsigned long lhs, const qfloat16 *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(const unsigned long &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKmRK8qfloat16(unsigned long lhs, const qfloat16 *rhs) {
  return operator!=(lhs, *rhs);
}

//  bool operator<(const unsigned long &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKmRK8qfloat16(unsigned long lhs, const qfloat16 *rhs) {
  return operator<(lhs, *rhs);
}

//  bool operator>(const unsigned long &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKmRK8qfloat16(unsigned long lhs, const qfloat16 *rhs) {
  return operator>(lhs, *rhs);
}

//  bool operator<=(const unsigned long &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKmRK8qfloat16(unsigned long lhs, const qfloat16 *rhs) {
  return operator<=(lhs, *rhs);
}

//  bool operator>=(const unsigned long &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKmRK8qfloat16(unsigned long lhs, const qfloat16 *rhs) {
  return operator>=(lhs, *rhs);
}

//  bool operator==(const qfloat16 &lhs, const qint64 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8qfloat16RKx(const qfloat16 *lhs, qint64 rhs) {
  return operator==(*lhs, rhs);
}

//  bool operator!=(const qfloat16 &lhs, const qint64 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8qfloat16RKx(const qfloat16 *lhs, qint64 rhs) {
  return operator!=(*lhs, rhs);
}

//  bool operator<(const qfloat16 &lhs, const qint64 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8qfloat16RKx(const qfloat16 *lhs, qint64 rhs) {
  return operator<(*lhs, rhs);
}

//  bool operator>(const qfloat16 &lhs, const qint64 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8qfloat16RKx(const qfloat16 *lhs, qint64 rhs) {
  return operator>(*lhs, rhs);
}

//  bool operator<=(const qfloat16 &lhs, const qint64 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8qfloat16RKx(const qfloat16 *lhs, qint64 rhs) {
  return operator<=(*lhs, rhs);
}

//  bool operator>=(const qfloat16 &lhs, const qint64 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8qfloat16RKx(const qfloat16 *lhs, qint64 rhs) {
  return operator>=(*lhs, rhs);
}

//  bool operator==(const qint64 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKxRK8qfloat16(qint64 lhs, const qfloat16 *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(const qint64 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKxRK8qfloat16(qint64 lhs, const qfloat16 *rhs) {
  return operator!=(lhs, *rhs);
}

//  bool operator<(const qint64 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKxRK8qfloat16(qint64 lhs, const qfloat16 *rhs) {
  return operator<(lhs, *rhs);
}

//  bool operator>(const qint64 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKxRK8qfloat16(qint64 lhs, const qfloat16 *rhs) {
  return operator>(lhs, *rhs);
}

//  bool operator<=(const qint64 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKxRK8qfloat16(qint64 lhs, const qfloat16 *rhs) {
  return operator<=(lhs, *rhs);
}

//  bool operator>=(const qint64 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKxRK8qfloat16(qint64 lhs, const qfloat16 *rhs) {
  return operator>=(lhs, *rhs);
}

//  bool operator==(const qfloat16 &lhs, const quint64 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8qfloat16RKy(const qfloat16 *lhs, quint64 rhs) {
  return operator==(*lhs, rhs);
}

//  bool operator!=(const qfloat16 &lhs, const quint64 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8qfloat16RKy(const qfloat16 *lhs, quint64 rhs) {
  return operator!=(*lhs, rhs);
}

//  bool operator<(const qfloat16 &lhs, const quint64 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8qfloat16RKy(const qfloat16 *lhs, quint64 rhs) {
  return operator<(*lhs, rhs);
}

//  bool operator>(const qfloat16 &lhs, const quint64 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8qfloat16RKy(const qfloat16 *lhs, quint64 rhs) {
  return operator>(*lhs, rhs);
}

//  bool operator<=(const qfloat16 &lhs, const quint64 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8qfloat16RKy(const qfloat16 *lhs, quint64 rhs) {
  return operator<=(*lhs, rhs);
}

//  bool operator>=(const qfloat16 &lhs, const quint64 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8qfloat16RKy(const qfloat16 *lhs, quint64 rhs) {
  return operator>=(*lhs, rhs);
}

//  bool operator==(const quint64 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKyRK8qfloat16(quint64 lhs, const qfloat16 *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(const quint64 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKyRK8qfloat16(quint64 lhs, const qfloat16 *rhs) {
  return operator!=(lhs, *rhs);
}

//  bool operator<(const quint64 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKyRK8qfloat16(quint64 lhs, const qfloat16 *rhs) {
  return operator<(lhs, *rhs);
}

//  bool operator>(const quint64 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKyRK8qfloat16(quint64 lhs, const qfloat16 *rhs) {
  return operator>(lhs, *rhs);
}

//  bool operator<=(const quint64 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKyRK8qfloat16(quint64 lhs, const qfloat16 *rhs) {
  return operator<=(lhs, *rhs);
}

//  bool operator>=(const quint64 &lhs, const qfloat16 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKyRK8qfloat16(quint64 lhs, const qfloat16 *rhs) {
  return operator>=(lhs, *rhs);
}

//  qfloat16::~qfloat16()
extern "C" Q_DECL_EXPORT
void ritual_ZN8qfloat16D1Ev(qfloat16 *self) {
  delete self;
}
