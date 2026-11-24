//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QAccessibleViewportInterface that Python can take functions over in. Every QAccessibleViewportInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef const QSizeF * (*CuteQAccessibleViewportInterfaceCall0)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QPointF * (*CuteQAccessibleViewportInterfaceCall1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QSizeF * (*CuteQAccessibleViewportInterfaceCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleViewportInterfaceCall3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleViewportInterfaceCall4)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleViewportInterface : public QAccessibleViewportInterface {
public:
  using QAccessibleViewportInterface::QAccessibleViewportInterface;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK28QAccessibleViewportInterface11contentSizeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK28QAccessibleViewportInterface8positionEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK28QAccessibleViewportInterface12viewportSizeEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK28QAccessibleViewportInterface9isIndexedEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN28QAccessibleViewportInterface11setPositionE7QPointF")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
  //  QSizeF QAccessibleViewportInterface::contentSize() const
  QSizeF contentSize() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleViewportInterfaceCall0 call = reinterpret_cast<CuteQAccessibleViewportInterfaceCall0>(taken[0]);
      const QSizeF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QPointF QAccessibleViewportInterface::position() const
  QPointF position() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleViewportInterfaceCall1 call = reinterpret_cast<CuteQAccessibleViewportInterfaceCall1>(taken[1]);
      const QPointF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QSizeF QAccessibleViewportInterface::viewportSize() const
  QSizeF viewportSize() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleViewportInterfaceCall2 call = reinterpret_cast<CuteQAccessibleViewportInterfaceCall2>(taken[2]);
      const QSizeF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleViewportInterface::isIndexed() const
  bool isIndexed() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleViewportInterfaceCall3 call = reinterpret_cast<CuteQAccessibleViewportInterfaceCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleViewportInterface::setPosition(QPointF position)
  void setPosition(QPointF position) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleViewportInterfaceCall4 call = reinterpret_cast<CuteQAccessibleViewportInterfaceCall4>(taken[4]);
      call(this, &position, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(accessibility)
};

//  QAccessibleViewportInterface::~QAccessibleViewportInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QAccessibleViewportInterfaceD1Ev(
    QAccessibleViewportInterface *self) {
  delete self;
}

//  QSizeF QAccessibleViewportInterface::contentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK28QAccessibleViewportInterface11contentSizeEv(
    const QAccessibleViewportInterface *self) {
  return new QSizeF(self->contentSize());
}

//  QPointF QAccessibleViewportInterface::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK28QAccessibleViewportInterface8positionEv(
    const QAccessibleViewportInterface *self) {
  return new QPointF(self->position());
}

//  QSizeF QAccessibleViewportInterface::viewportSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK28QAccessibleViewportInterface12viewportSizeEv(
    const QAccessibleViewportInterface *self) {
  return new QSizeF(self->viewportSize());
}

//  bool QAccessibleViewportInterface::isIndexed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QAccessibleViewportInterface9isIndexedEv(
    const QAccessibleViewportInterface *self) {
  return self->isIndexed();
}

//  void QAccessibleViewportInterface::setPosition(QPointF position)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QAccessibleViewportInterface11setPositionE7QPointF(
    QAccessibleViewportInterface *self,
    const QPointF *position) {
  self->setPosition(*position);
}

//  a Python function taken by a CuteQAccessibleViewportInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleViewportInterface(
    QAccessibleViewportInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleViewportInterface *>(self)->take(key, call);
}

#endif  // QT_CONFIG(accessibility)
