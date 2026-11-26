//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpainterstateguard.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpainterstateguard.h>

//  QPainterStateGuard::QPainterStateGuard(QPainterStateGuard &&other)
extern "C" Q_DECL_EXPORT
QPainterStateGuard *ritual_ZN18QPainterStateGuardC1EOS_(
    QPainterStateGuard *other) {
  return new QPainterStateGuard(std::move(*other));
}

//  QPainterStateGuard &QPainterStateGuard::operator=(QPainterStateGuard
//      &&other)
extern "C" Q_DECL_EXPORT
QPainterStateGuard *ritual_ZN18QPainterStateGuardaSEOS_(
    QPainterStateGuard *self,
    QPainterStateGuard *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QPainterStateGuard::swap(QPainterStateGuard &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPainterStateGuard4swapERS_(
    QPainterStateGuard *self,
    QPainterStateGuard *other) {
  self->swap(*other);
}

//  QPainterStateGuard::QPainterStateGuard(QPainter *painter, InitialState
//      state)
extern "C" Q_DECL_EXPORT
QPainterStateGuard *ritual_ZN18QPainterStateGuardC1EP8QPainterNS_12InitialStateE(
    QPainter *painter,
    QPainterStateGuard::InitialState state) {
  return new QPainterStateGuard(painter, state);
}

//  QPainterStateGuard::~QPainterStateGuard()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPainterStateGuardD1Ev(QPainterStateGuard *self) {
  delete self;
}

//  void QPainterStateGuard::save()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPainterStateGuard4saveEv(QPainterStateGuard *self) {
  self->save();
}

//  void QPainterStateGuard::restore()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPainterStateGuard7restoreEv(QPainterStateGuard *self) {
  self->restore();
}

//  void QPainterStateGuard::verifyPainter()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPainterStateGuard13verifyPainterEv(
    QPainterStateGuard *self) {
  self->verifyPainter();
}
