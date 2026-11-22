//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpoint.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>

//  QPointF::QPointF()
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN7QPointFC1Ev() {
  return new QPointF();
}

//  QPointF::QPointF(const QPoint &p)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN7QPointFC1ERK6QPoint(const QPoint *p) {
  return new QPointF(*p);
}

//  QPointF::QPointF(qreal xpos, qreal ypos)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN7QPointFC1Edd(qreal xpos, qreal ypos) {
  return new QPointF(xpos, ypos);
}

//  qreal QPointF::manhattanLength() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QPointF15manhattanLengthEv(const QPointF *self) {
  return self->manhattanLength();
}

//  bool QPointF::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QPointF6isNullEv(const QPointF *self) {
  return self->isNull();
}

//  qreal QPointF::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QPointF1xEv(const QPointF *self) {
  return self->x();
}

//  qreal QPointF::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QPointF1yEv(const QPointF *self) {
  return self->y();
}

//  void QPointF::setX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPointF4setXEd(QPointF *self, qreal x) {
  self->setX(x);
}

//  void QPointF::setY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPointF4setYEd(QPointF *self, qreal y) {
  self->setY(y);
}

//  QPointF QPointF::transposed() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QPointF10transposedEv(const QPointF *self) {
  return new QPointF(self->transposed());
}

//  QPointF &QPointF::operator+=(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPointFpLERKS_(QPointF *self, const QPointF *p) {
  self->operator+=(*p);
}

//  QPointF &QPointF::operator-=(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPointFmIERKS_(QPointF *self, const QPointF *p) {
  self->operator-=(*p);
}

//  QPointF &QPointF::operator*=(qreal c)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPointFmLEd(QPointF *self, qreal c) {
  self->operator*=(c);
}

//  QPointF &QPointF::operator/=(qreal c)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPointFdVEd(QPointF *self, qreal c) {
  self->operator/=(c);
}

//  qreal QPointF::dotProduct(const QPointF &p1, const QPointF &p2)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN7QPointF10dotProductERKS_S1_(
    const QPointF *p1,
    const QPointF *p2) {
  return QPointF::dotProduct(*p1, *p2);
}

//  bool operator==(const QPointF &lhs, const QPointF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK7QPointFS1_(const QPointF *lhs, const QPointF *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPointF &lhs, const QPointF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK7QPointFS1_(const QPointF *lhs, const QPointF *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QPointF &lhs, const QPoint &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK7QPointFRK6QPoint(const QPointF *lhs, const QPoint *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPointF &lhs, const QPoint &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK7QPointFRK6QPoint(const QPointF *lhs, const QPoint *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QPoint &lhs, const QPointF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK6QPointRK7QPointF(const QPoint *lhs, const QPointF *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPoint &lhs, const QPointF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK6QPointRK7QPointF(const QPoint *lhs, const QPointF *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QPointF operator+(const QPointF &p1, const QPointF &p2)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZplRK7QPointFS1_(const QPointF *p1, const QPointF *p2) {
  return new QPointF(operator+(*p1, *p2));
}

//  QPointF operator-(const QPointF &p1, const QPointF &p2)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZmiRK7QPointFS1_(const QPointF *p1, const QPointF *p2) {
  return new QPointF(operator-(*p1, *p2));
}

//  QPointF operator*(const QPointF &p, qreal c)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZmlRK7QPointFd(const QPointF *p, qreal c) {
  return new QPointF(operator*(*p, c));
}

//  QPointF operator*(qreal c, const QPointF &p)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZmldRK7QPointF(qreal c, const QPointF *p) {
  return new QPointF(operator*(c, *p));
}

//  QPointF operator+(const QPointF &p)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZpsRK7QPointF(const QPointF *p) {
  return new QPointF(operator+(*p));
}

//  QPointF operator-(const QPointF &p)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZngRK7QPointF(const QPointF *p) {
  return new QPointF(operator-(*p));
}

//  QPointF operator/(const QPointF &p, qreal divisor)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZdvRK7QPointFd(const QPointF *p, qreal divisor) {
  return new QPointF(operator/(*p, divisor));
}

//  QPoint QPointF::toPoint() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QPointF7toPointEv(const QPointF *self) {
  return new QPoint(self->toPoint());
}

//  QPointF::~QPointF()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPointFD1Ev(QPointF *self) {
  delete self;
}

//  QList<QPointF>::QList()
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_list_make_QPointF() {
  return new QList<QPointF>();
}

//  void QList<QPointF>::append(const QPointF &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QPointF(QList<QPointF> *self, const QPointF *element) {
  self->append(*element);
}

//  qsizetype QList<QPointF>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QPointF(const QList<QPointF> *self) {
  return self->size();
}

//  const QPointF &QList<QPointF>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_list_at_QPointF(
    const QList<QPointF> *self,
    long long index) {
  return new QPointF(self->at(index));
}

//  QList<QPointF>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QPointF(QList<QPointF> *self) {
  delete self;
}
