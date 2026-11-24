//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickselectable_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_tableview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickselectable_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QQuickSelectable that Python can take functions over in. Every QQuickSelectable
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickSelectableCall0)(const void *, int *);
typedef bool (*CuteQQuickSelectableCall1)(const void *, int *);
typedef bool (*CuteQQuickSelectableCall2)(const void *, const QPointF *, int, int *);
typedef void (*CuteQQuickSelectableCall3)(const void *, const QPointF *, int *);
typedef void (*CuteQQuickSelectableCall4)(const void *, const QPointF *, int *);
typedef void (*CuteQQuickSelectableCall5)(const void *, int *);
typedef void (*CuteQQuickSelectableCall6)(const void *, int *);
typedef const QRectF * (*CuteQQuickSelectableCall7)(const void *, int *);
typedef const QSizeF * (*CuteQQuickSelectableCall8)(const void *, const QPointF *, const QSizeF *, int *);
class CuteQQuickSelectable : public QQuickSelectable {
public:
  using QQuickSelectable::QQuickSelectable;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QQuickSelectable29selectionPointerHandlerTargetEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickSelectable12hasSelectionEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable14startSelectionERK7QPointF6QFlagsIN2Qt16KeyboardModifierEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable20setSelectionStartPosERK7QPointF")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable18setSelectionEndPosERK7QPointF")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable14clearSelectionEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable18normalizeSelectionEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickSelectable18selectionRectangleEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickSelectable18scrollTowardsPointERK7QPointFRK6QSizeF")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  QQuickItem *QQuickSelectable::selectionPointerHandlerTarget() const
  QQuickItem *selectionPointerHandlerTarget() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSelectableCall0 call = reinterpret_cast<CuteQQuickSelectableCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return {};
  }

  //  bool QQuickSelectable::hasSelection() const
  bool hasSelection() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSelectableCall1 call = reinterpret_cast<CuteQQuickSelectableCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QQuickSelectable::startSelection(const QPointF &pos,
  //      Qt::KeyboardModifiers modifiers)
  bool startSelection(
      const QPointF &pos,
      Qt::KeyboardModifiers modifiers) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSelectableCall2 call = reinterpret_cast<CuteQQuickSelectableCall2>(taken[2]);
      bool given = call(this, &pos, static_cast<int>(modifiers.toInt()), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQuickSelectable::setSelectionStartPos(const QPointF &pos)
  void setSelectionStartPos(const QPointF &pos) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickSelectableCall3 call = reinterpret_cast<CuteQQuickSelectableCall3>(taken[3]);
      call(this, &pos, &handled);
      if (handled) return;
    }
  }

  //  void QQuickSelectable::setSelectionEndPos(const QPointF &pos)
  void setSelectionEndPos(const QPointF &pos) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickSelectableCall4 call = reinterpret_cast<CuteQQuickSelectableCall4>(taken[4]);
      call(this, &pos, &handled);
      if (handled) return;
    }
  }

  //  void QQuickSelectable::clearSelection()
  void clearSelection() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickSelectableCall5 call = reinterpret_cast<CuteQQuickSelectableCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QQuickSelectable::normalizeSelection()
  void normalizeSelection() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickSelectableCall6 call = reinterpret_cast<CuteQQuickSelectableCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QRectF QQuickSelectable::selectionRectangle() const
  QRectF selectionRectangle() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickSelectableCall7 call = reinterpret_cast<CuteQQuickSelectableCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QSizeF QQuickSelectable::scrollTowardsPoint(const QPointF &pos, const
  //      QSizeF &step)
  QSizeF scrollTowardsPoint(
      const QPointF &pos,
      const QSizeF &step) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickSelectableCall8 call = reinterpret_cast<CuteQQuickSelectableCall8>(taken[8]);
      const QSizeF * given = call(this, &pos, &step, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QQuickSelectable::~QQuickSelectable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickSelectableD1Ev(QQuickSelectable *self) {
  delete self;
}

//  QQuickItem *QQuickSelectable::selectionPointerHandlerTarget() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK16QQuickSelectable29selectionPointerHandlerTargetEv(
    const QQuickSelectable *self) {
  return self->selectionPointerHandlerTarget();
}

//  bool QQuickSelectable::hasSelection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickSelectable12hasSelectionEv(
    const QQuickSelectable *self) {
  return self->hasSelection();
}

//  bool QQuickSelectable::startSelection(const QPointF &pos,
//      Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickSelectable14startSelectionERK7QPointF6QFlagsIN2Qt16KeyboardModifierEE(
    QQuickSelectable *self,
    const QPointF *pos,
    int modifiers) {
  return self->startSelection(
      *pos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  void QQuickSelectable::setSelectionStartPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickSelectable20setSelectionStartPosERK7QPointF(
    QQuickSelectable *self,
    const QPointF *pos) {
  self->setSelectionStartPos(*pos);
}

//  void QQuickSelectable::setSelectionEndPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickSelectable18setSelectionEndPosERK7QPointF(
    QQuickSelectable *self,
    const QPointF *pos) {
  self->setSelectionEndPos(*pos);
}

//  void QQuickSelectable::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickSelectable14clearSelectionEv(QQuickSelectable *self) {
  self->clearSelection();
}

//  void QQuickSelectable::normalizeSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickSelectable18normalizeSelectionEv(
    QQuickSelectable *self) {
  self->normalizeSelection();
}

//  QRectF QQuickSelectable::selectionRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16QQuickSelectable18selectionRectangleEv(
    const QQuickSelectable *self) {
  return new QRectF(self->selectionRectangle());
}

//  QSizeF QQuickSelectable::scrollTowardsPoint(const QPointF &pos, const
//      QSizeF &step)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZN16QQuickSelectable18scrollTowardsPointERK7QPointFRK6QSizeF(
    QQuickSelectable *self,
    const QPointF *pos,
    const QSizeF *step) {
  return new QSizeF(self->scrollTowardsPoint(*pos, *step));
}

//  a Python function taken by a CuteQQuickSelectable, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSelectable(
    QQuickSelectable *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSelectable *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_tableview)
