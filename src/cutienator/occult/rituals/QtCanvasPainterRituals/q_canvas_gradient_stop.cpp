//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvasgradient.h, Qt 6.12.0. Changes made here are lost.
#include <QtCanvasPainter/qcanvasgradient.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  bool operator==(const QCanvasGradientStop &lhs, const QCanvasGradientStop
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK19QCanvasGradientStopS1_(
    const QCanvasGradientStop *lhs,
    const QCanvasGradientStop *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCanvasGradientStop &lhs, const QCanvasGradientStop
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK19QCanvasGradientStopS1_(
    const QCanvasGradientStop *lhs,
    const QCanvasGradientStop *rhs) {
  return operator!=(*lhs, *rhs);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const QCanvasGradientStop &stop)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK19QCanvasGradientStop(
    const QDebug *dbg,
    const QCanvasGradientStop *stop) {
  return new QDebug(operator<<(*dbg, *stop));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator<<(QDataStream &a0, const QCanvasGradientStop &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK19QCanvasGradientStop(
    QDataStream *a0,
    const QCanvasGradientStop *a1) {
  return &(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator>>(QDataStream &a0, QCanvasGradientStop &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR19QCanvasGradientStop(
    QDataStream *a0,
    QCanvasGradientStop *a1) {
  return &(operator>>(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

//  QCanvasGradientStop::~QCanvasGradientStop()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasGradientStopD1Ev(QCanvasGradientStop *self) {
  delete self;
}

//  QList<QCanvasGradientStop>::QList()
extern "C" Q_DECL_EXPORT
QList<QCanvasGradientStop> *ritual_list_make_QCanvasGradientStop() {
  return new QList<QCanvasGradientStop>();
}

//  void QList<QCanvasGradientStop>::append(const QCanvasGradientStop &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCanvasGradientStop(
    QList<QCanvasGradientStop> *self,
    const QCanvasGradientStop *element) {
  self->append(*element);
}

//  qsizetype QList<QCanvasGradientStop>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCanvasGradientStop(
    const QList<QCanvasGradientStop> *self) {
  return self->size();
}

//  const QCanvasGradientStop &QList<QCanvasGradientStop>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QCanvasGradientStop *ritual_list_at_QCanvasGradientStop(
    const QList<QCanvasGradientStop> *self,
    long long index) {
  return new QCanvasGradientStop(self->at(index));
}

//  QList<QCanvasGradientStop>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCanvasGradientStop(QList<QCanvasGradientStop> *self) {
  delete self;
}
