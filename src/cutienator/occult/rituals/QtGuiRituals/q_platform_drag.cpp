//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformdrag.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformdrag.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpixmap.h>
#include <cstring>

//  A QPlatformDrag that Python can take functions over in. Every QPlatformDrag
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(draganddrop)
typedef int (*CuteQPlatformDragCall0)(const void *, QDrag *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQPlatformDragCall1)(const void *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef int (*CuteQPlatformDragCall2)(const void *, int, int, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef bool (*CuteQPlatformDragCall3)(const void *, int *);
#endif  // QT_CONFIG(draganddrop)
class CuteQPlatformDrag : public QPlatformDrag {
public:
  using QPlatformDrag::QPlatformDrag;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN13QPlatformDrag4dragEP5QDrag")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN13QPlatformDrag10cancelDragEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZNK13QPlatformDrag13defaultActionE6QFlagsIN2Qt10DropActionEES0_INS1_16KeyboardModifierEE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZNK13QPlatformDrag14ownsDragObjectEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    return false;
  }

#if QT_CONFIG(draganddrop)
  //  Qt::DropAction QPlatformDrag::drag(QDrag *m_drag)
  Qt::DropAction drag(QDrag *m_drag) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformDragCall0 call = reinterpret_cast<CuteQPlatformDragCall0>(taken[0]);
      int given = call(this, m_drag, &handled);
      if (handled) return static_cast<Qt::DropAction>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QPlatformDrag::cancelDrag()
  void cancelDrag() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformDragCall1 call = reinterpret_cast<CuteQPlatformDragCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformDrag::cancelDrag();
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  Qt::DropAction QPlatformDrag::defaultAction(Qt::DropActions
  //      possibleActions, Qt::KeyboardModifiers modifiers) const
  Qt::DropAction defaultAction(
      Qt::DropActions possibleActions,
      Qt::KeyboardModifiers modifiers) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformDragCall2 call = reinterpret_cast<CuteQPlatformDragCall2>(taken[2]);
      int given = call(this, static_cast<int>(possibleActions.toInt()), static_cast<int>(modifiers.toInt()), &handled);
      if (handled) return static_cast<Qt::DropAction>(given);
    }
    return QPlatformDrag::defaultAction(possibleActions, modifiers);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  bool QPlatformDrag::ownsDragObject() const
  bool ownsDragObject() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformDragCall3 call = reinterpret_cast<CuteQPlatformDragCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformDrag::ownsDragObject();
  }
#endif  // QT_CONFIG(draganddrop)
};

//  QPlatformDrag::~QPlatformDrag()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformDragD1Ev(QPlatformDrag *self) {
  delete self;
}

//  QDrag *QPlatformDrag::currentDrag() const
extern "C" Q_DECL_EXPORT
QDrag *ritual_ZNK13QPlatformDrag11currentDragEv(const QPlatformDrag *self) {
  return self->currentDrag();
}

//  Qt::DropAction QPlatformDrag::drag(QDrag *m_drag)
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZN13QPlatformDrag4dragEP5QDrag(
    QPlatformDrag *self,
    QDrag *m_drag) {
  return self->drag(m_drag);
}

//  void QPlatformDrag::cancelDrag()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformDrag10cancelDragEv(QPlatformDrag *self) {
  self->cancelDrag();
}

//  void QPlatformDrag::updateAction(Qt::DropAction action)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformDrag12updateActionEN2Qt10DropActionE(
    QPlatformDrag *self,
    Qt::DropAction action) {
  self->updateAction(action);
}

//  Qt::DropAction QPlatformDrag::defaultAction(Qt::DropActions
//      possibleActions, Qt::KeyboardModifiers modifiers) const
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZNK13QPlatformDrag13defaultActionE6QFlagsIN2Qt10DropActionEES0_INS1_16KeyboardModifierEE(
    const QPlatformDrag *self,
    int possibleActions,
    int modifiers) {
  return self->defaultAction(
      QFlags<Qt::DropAction>::fromInt(possibleActions),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  QPixmap QPlatformDrag::defaultPixmap()
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN13QPlatformDrag13defaultPixmapEv() {
  return new QPixmap(QPlatformDrag::defaultPixmap());
}

//  bool QPlatformDrag::ownsDragObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPlatformDrag14ownsDragObjectEv(const QPlatformDrag *self) {
  return self->ownsDragObject();
}

//  a Python function taken by a CuteQPlatformDrag, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformDrag(
    QPlatformDrag *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformDrag *>(self)->take(key, call);
}

//  void QPlatformDrag::cancelDrag()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QPlatformDrag10cancelDragEv(QPlatformDrag *self) {
  self->QPlatformDrag::cancelDrag();
}

//  Qt::DropAction QPlatformDrag::defaultAction(Qt::DropActions
//      possibleActions, Qt::KeyboardModifiers modifiers) const
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_own_ZNK13QPlatformDrag13defaultActionE6QFlagsIN2Qt10DropActionEES0_INS1_16KeyboardModifierEE(
    const QPlatformDrag *self,
    int possibleActions,
    int modifiers) {
  return self->QPlatformDrag::defaultAction(
      QFlags<Qt::DropAction>::fromInt(possibleActions),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  bool QPlatformDrag::ownsDragObject() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QPlatformDrag14ownsDragObjectEv(
    const QPlatformDrag *self) {
  return self->QPlatformDrag::ownsDragObject();
}

#endif  // QT_CONFIG(draganddrop)
