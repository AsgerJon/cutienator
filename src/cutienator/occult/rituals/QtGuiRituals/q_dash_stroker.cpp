//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qstroker_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qstroker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#include <QtCore/QList>

//  Only a class built on QDashStroker may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDashStroker : QDashStroker {
  using QDashStroker::processCurrentSubpath;
};

//  A QDashStroker that Python can take functions over in. Every QDashStroker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDashStrokerCall0)(const void *, void *, int *);
typedef void (*CuteQDashStrokerCall1)(const void *, int *);
typedef void (*CuteQDashStrokerCall2)(const void *, int *);
class CuteQDashStroker : public QDashStroker {
public:
  using QDashStroker::QDashStroker;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN11QStrokerOps5beginEPv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QStrokerOps3endEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QStrokerOps21processCurrentSubpathEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QDashStroker::begin(void *data)
  void begin(void *data) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDashStrokerCall0 call = reinterpret_cast<CuteQDashStrokerCall0>(taken[0]);
      call(this, data, &handled);
      if (handled) return;
    }
    QDashStroker::begin(data);
  }

  //  void QDashStroker::end()
  void end() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDashStrokerCall1 call = reinterpret_cast<CuteQDashStrokerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDashStroker::end();
  }

  //  void QDashStroker::processCurrentSubpath()
  void processCurrentSubpath() override {
    if (taken[2]) {
      int handled = 0;
      CuteQDashStrokerCall2 call = reinterpret_cast<CuteQDashStrokerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QDashStroker::processCurrentSubpath();
  }
};

//  QDashStroker::QDashStroker(QStroker *stroker)
extern "C" Q_DECL_EXPORT
QDashStroker *ritual_ZN12QDashStrokerC1EP8QStroker(QStroker *stroker) {
  return new CuteQDashStroker(stroker);
}

//  QDashStroker::~QDashStroker()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDashStrokerD1Ev(QDashStroker *self) {
  delete self;
}

//  QStroker *QDashStroker::stroker() const
extern "C" Q_DECL_EXPORT
QStroker *ritual_ZNK12QDashStroker7strokerEv(const QDashStroker *self) {
  return self->stroker();
}

//  QList<qfixed> QDashStroker::patternForStyle(Qt::PenStyle style)
extern "C" Q_DECL_EXPORT
QList<qfixed> *ritual_ZN12QDashStroker15patternForStyleEN2Qt8PenStyleE(
    Qt::PenStyle style) {
  return new QList<qfixed>(QDashStroker::patternForStyle(style));
}

//  int QDashStroker::repetitionLimit()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QDashStroker15repetitionLimitEv() {
  return QDashStroker::repetitionLimit();
}

//  void QDashStroker::setDashPattern(const QList<qfixed> &dashPattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDashStroker14setDashPatternERK5QListIdE(
    QDashStroker *self,
    const QList<qfixed> *dashPattern) {
  self->setDashPattern(*dashPattern);
}

//  QList<qfixed> QDashStroker::dashPattern() const
extern "C" Q_DECL_EXPORT
QList<qfixed> *ritual_ZNK12QDashStroker11dashPatternEv(
    const QDashStroker *self) {
  return new QList<qfixed>(self->dashPattern());
}

//  void QDashStroker::setDashOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDashStroker13setDashOffsetEd(
    QDashStroker *self,
    qreal offset) {
  self->setDashOffset(offset);
}

//  qreal QDashStroker::dashOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QDashStroker10dashOffsetEv(const QDashStroker *self) {
  return self->dashOffset();
}

//  void QDashStroker::begin(void *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDashStroker5beginEPv(QDashStroker *self, void *data) {
  self->begin(data);
}

//  void QDashStroker::end()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDashStroker3endEv(QDashStroker *self) {
  self->end();
}

//  void QDashStroker::setStrokeWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDashStroker14setStrokeWidthEd(
    QDashStroker *self,
    qreal width) {
  self->setStrokeWidth(width);
}

//  void QDashStroker::setMiterLimit(qreal limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDashStroker13setMiterLimitEd(
    QDashStroker *self,
    qreal limit) {
  self->setMiterLimit(limit);
}

//  void QDashStroker::processCurrentSubpath()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDashStroker21processCurrentSubpathEv(QDashStroker *self) {
  self->processCurrentSubpath();
}

//  a Python function taken by a CuteQDashStroker, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDashStroker(
    QDashStroker *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDashStroker *>(self)->take(key, call);
}

//  void QDashStroker::begin(void *data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QDashStroker5beginEPv(QDashStroker *self, void *data) {
  self->QDashStroker::begin(data);
}

//  void QDashStroker::end()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QDashStroker3endEv(QDashStroker *self) {
  self->QDashStroker::end();
}

//  void QDashStroker::processCurrentSubpath()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QDashStroker21processCurrentSubpathEv(
    QDashStroker *self) {
  static_cast<OwnQDashStroker *>(self)->OwnQDashStroker::processCurrentSubpath();
}

//  a QList<qfixed> a ritual of QDashStroker gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDashStroker__QList_qfixed(QList<qfixed> *self) {
  delete self;
}
