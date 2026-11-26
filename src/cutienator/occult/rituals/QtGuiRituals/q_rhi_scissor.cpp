//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <array>

//  QRhiScissor::QRhiScissor()
extern "C" Q_DECL_EXPORT
QRhiScissor *ritual_ZN11QRhiScissorC1Ev() {
  return new QRhiScissor();
}

//  QRhiScissor::QRhiScissor(int x, int y, int w, int h)
extern "C" Q_DECL_EXPORT
QRhiScissor *ritual_ZN11QRhiScissorC1Eiiii(int x, int y, int w, int h) {
  return new QRhiScissor(x, y, w, h);
}

//  std::array<int, 4> QRhiScissor::scissor() const
extern "C" Q_DECL_EXPORT
std::array<int, 4> *ritual_ZNK11QRhiScissor7scissorEv(
    const QRhiScissor *self) {
  return new std::array<int, 4>(self->scissor());
}

//  void QRhiScissor::setScissor(int x, int y, int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiScissor10setScissorEiiii(
    QRhiScissor *self,
    int x,
    int y,
    int w,
    int h) {
  self->setScissor(x, y, w, h);
}

//  bool operator==(const QRhiScissor &a, const QRhiScissor &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QRhiScissorS1_(
    const QRhiScissor *a,
    const QRhiScissor *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QRhiScissor &a, const QRhiScissor &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QRhiScissorS1_(
    const QRhiScissor *a,
    const QRhiScissor *b) {
  return operator!=(*a, *b);
}

//  QRhiScissor::~QRhiScissor()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiScissorD1Ev(QRhiScissor *self) {
  delete self;
}

//  a std::array<int, 4> a ritual of QRhiScissor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QRhiScissor__std_array_int_4(std::array<int, 4> *self) {
  delete self;
}
