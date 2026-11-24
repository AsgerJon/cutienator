//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvasbrush.h, Qt 6.12.0. Changes made here are lost.
#include <QtCanvasPainter/qcanvasbrush.h>
#include <QtCore/qdebug.h>

//  QCanvasBrush::QCanvasBrush()
extern "C" Q_DECL_EXPORT
QCanvasBrush *ritual_ZN12QCanvasBrushC1Ev() {
  return new QCanvasBrush();
}

//  QCanvasBrush::QCanvasBrush(const QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasBrush *ritual_ZN12QCanvasBrushC1ERKS_(const QCanvasBrush *brush) {
  return new QCanvasBrush(*brush);
}

//  QCanvasBrush::~QCanvasBrush()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanvasBrushD1Ev(QCanvasBrush *self) {
  delete self;
}

//  BrushType QCanvasBrush::type() const
extern "C" Q_DECL_EXPORT
QCanvasBrush::BrushType ritual_ZNK12QCanvasBrush4typeEv(
    const QCanvasBrush *self) {
  return self->type();
}

//  bool operator==(const QCanvasBrush &lhs, const QCanvasBrush &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK12QCanvasBrushS1_(
    const QCanvasBrush *lhs,
    const QCanvasBrush *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCanvasBrush &lhs, const QCanvasBrush &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK12QCanvasBrushS1_(
    const QCanvasBrush *lhs,
    const QCanvasBrush *rhs) {
  return operator!=(*lhs, *rhs);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QCanvasBrush &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK12QCanvasBrush(
    const QDebug *a0,
    const QCanvasBrush *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
