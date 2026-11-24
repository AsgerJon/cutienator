//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qaccessiblequickflickable_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(accessibility)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qaccessiblequickflickable_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>
#include <cstring>

//  A QAccessibleQuickFlickable that Python can take functions over in. Every QAccessibleQuickFlickable
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef const QSizeF * (*CuteQAccessibleQuickFlickableCall0)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QPointF * (*CuteQAccessibleQuickFlickableCall1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QSizeF * (*CuteQAccessibleQuickFlickableCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleQuickFlickableCall3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickFlickableCall4)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleQuickFlickableCall5)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickFlickableCall6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleQuickFlickableCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickFlickableCall8)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickFlickableCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickFlickableCall10)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickFlickableCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickFlickableCall12)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleQuickFlickableCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickFlickableCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickFlickableCall15)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickFlickableCall16)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickFlickableCall17)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickFlickableCall18)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickFlickableCall19)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickFlickableCall20)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickFlickableCall21)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickFlickableCall22)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickFlickableCall23)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickFlickableCall24)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickFlickableCall25)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickFlickableCall26)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickFlickableCall27)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickFlickableCall28)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickFlickableCall29)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickFlickableCall30)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleQuickFlickableCall31)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickFlickableCall32)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickFlickableCall33)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickFlickableCall34)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickFlickableCall35)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickFlickableCall36)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleQuickFlickableCall37)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleQuickFlickableCall38)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickFlickableCall39)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickFlickableCall40)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleQuickFlickable : public QAccessibleQuickFlickable {
public:
  using QAccessibleQuickFlickable::QAccessibleQuickFlickable;
  void *taken[41] = {};

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
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12currentValueEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN25QAccessibleValueInterface15setCurrentValueERK8QVariant")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12maximumValueEv")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12minimumValueEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface15minimumStepSizeEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14selectionCountEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12addSelectionEii")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface15removeSelectionEi")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12setSelectionEiii")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14cursorPositionEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17setCursorPositionEi")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface4textEii")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14characterCountEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13characterRectEi")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13offsetAtPointERK6QPoint")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17scrollToSubstringEii")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
  //  QSizeF QAccessibleQuickFlickable::contentSize() const
  QSizeF contentSize() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall0 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall0>(taken[0]);
      const QSizeF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickFlickable::contentSize();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QPointF QAccessibleQuickFlickable::position() const
  QPointF position() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall1 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall1>(taken[1]);
      const QPointF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickFlickable::position();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QSizeF QAccessibleQuickFlickable::viewportSize() const
  QSizeF viewportSize() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall2 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall2>(taken[2]);
      const QSizeF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickFlickable::viewportSize();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleQuickFlickable::isIndexed() const
  bool isIndexed() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall3 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickFlickable::isIndexed();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickFlickable::setPosition(QPointF position)
  void setPosition(QPointF position) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall4 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall4>(taken[4]);
      call(this, &position, &handled);
      if (handled) return;
    }
    QAccessibleQuickFlickable::setPosition(position);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleQuickItem::isValid() const
  bool isValid() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall5 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickItem::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleQuickItem::window() const
  QWindow *window() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall6 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleQuickItem::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleQuickItem::rect() const
  QRect rect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall7 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall7>(taken[7]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickItem::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleQuickItem::childAt(int x, int y)
  //      const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall8 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall8>(taken[8]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleQuickItem::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleQuickItem::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall9 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleQuickItem::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleQuickItem::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall10 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall10>(taken[10]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleQuickItem::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickItem::childCount() const
  int childCount() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall11 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickItem::childCount();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickItem::indexOfChild(const QAccessibleInterface
  //      *iface) const
  int indexOfChild(const QAccessibleInterface *iface) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall12 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall12>(taken[12]);
      int given = call(this, iface, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickItem::indexOfChild(iface);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleQuickItem::state() const
  QAccessible::State state() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall13 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall13>(taken[13]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickItem::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleQuickItem::role() const
  QAccessible::Role role() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall14 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleQuickItem::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleQuickItem::text(QAccessible::Text a0) const
  QString text(QAccessible::Text a0) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall15 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall15>(taken[15]);
      QString * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleQuickItem::text(a0);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::setText(QAccessible::Text a0, const
  //      QString &text)
  void setText(QAccessible::Text a0, const QString &text) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall16 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall16>(taken[16]);
      call(this, static_cast<int>(a0), &text, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::setText(a0, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall17 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall17>(taken[17]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleQuickItem::currentValue() const
  QVariant currentValue() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall18 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall18>(taken[18]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickItem::currentValue();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::setCurrentValue(const QVariant &value)
  void setCurrentValue(const QVariant &value) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall19 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall19>(taken[19]);
      call(this, &value, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::setCurrentValue(value);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleQuickItem::maximumValue() const
  QVariant maximumValue() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall20 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall20>(taken[20]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickItem::maximumValue();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleQuickItem::minimumValue() const
  QVariant minimumValue() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall21 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall21>(taken[21]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickItem::minimumValue();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleQuickItem::minimumStepSize() const
  QVariant minimumStepSize() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall22 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall22>(taken[22]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickItem::minimumStepSize();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickItem::selectionCount() const
  int selectionCount() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall23 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall23>(taken[23]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickItem::selectionCount();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::addSelection(int startOffset, int
  //      endOffset)
  void addSelection(int startOffset, int endOffset) override {
    if (taken[24]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall24 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall24>(taken[24]);
      call(this, startOffset, endOffset, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::addSelection(startOffset, endOffset);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::removeSelection(int selectionIndex)
  void removeSelection(int selectionIndex) override {
    if (taken[25]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall25 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall25>(taken[25]);
      call(this, selectionIndex, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::removeSelection(selectionIndex);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::setSelection(int selectionIndex, int
  //      startOffset, int endOffset)
  void setSelection(
      int selectionIndex,
      int startOffset,
      int endOffset) override {
    if (taken[26]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall26 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall26>(taken[26]);
      call(this, selectionIndex, startOffset, endOffset, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::setSelection(selectionIndex, startOffset, endOffset);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickItem::cursorPosition() const
  int cursorPosition() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall27 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall27>(taken[27]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickItem::cursorPosition();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::setCursorPosition(int position)
  void setCursorPosition(int position) override {
    if (taken[28]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall28 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall28>(taken[28]);
      call(this, position, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::setCursorPosition(position);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleQuickItem::text(int startOffset, int endOffset)
  //      const
  QString text(int startOffset, int endOffset) const override {
    if (taken[29]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall29 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall29>(taken[29]);
      QString * given = call(this, startOffset, endOffset, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleQuickItem::text(startOffset, endOffset);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickItem::characterCount() const
  int characterCount() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall30 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall30>(taken[30]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickItem::characterCount();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleQuickItem::characterRect(int a0) const
  QRect characterRect(int a0) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall31 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall31>(taken[31]);
      const QRect * given = call(this, a0, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickItem::characterRect(a0);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickItem::offsetAtPoint(const QPoint &a0) const
  int offsetAtPoint(const QPoint &a0) const override {
    if (taken[32]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall32 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall32>(taken[32]);
      int given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickItem::offsetAtPoint(a0);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::scrollToSubstring(int a0, int a1)
  void scrollToSubstring(int a0, int a1) override {
    if (taken[33]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall33 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall33>(taken[33]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::scrollToSubstring(a0, a1);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleQuickItem::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall34 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall34>(taken[34]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickItem::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall35 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall35>(taken[35]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleObject::object();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleInterface::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall36 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleInterface::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleInterface::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall37 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall37>(taken[37]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleInterface::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleInterface::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall38 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall38>(taken[38]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleInterface::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall39 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall39>(taken[39]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionName(name);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionDescription(const
  //      QString &name) const
  QString localizedActionDescription(const QString &name) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQAccessibleQuickFlickableCall40 call = reinterpret_cast<CuteQAccessibleQuickFlickableCall40>(taken[40]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionDescription(name);
  }
#endif  // QT_CONFIG(accessibility)
};

//  QAccessibleQuickFlickable::QAccessibleQuickFlickable(QQuickFlickable
//      *flickable)
extern "C" Q_DECL_EXPORT
QAccessibleQuickFlickable *ritual_ZN25QAccessibleQuickFlickableC1EP15QQuickFlickable(
    QQuickFlickable *flickable) {
  return new CuteQAccessibleQuickFlickable(flickable);
}

//  QSizeF QAccessibleQuickFlickable::contentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK25QAccessibleQuickFlickable11contentSizeEv(
    const QAccessibleQuickFlickable *self) {
  return new QSizeF(self->contentSize());
}

//  QPointF QAccessibleQuickFlickable::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK25QAccessibleQuickFlickable8positionEv(
    const QAccessibleQuickFlickable *self) {
  return new QPointF(self->position());
}

//  QSizeF QAccessibleQuickFlickable::viewportSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK25QAccessibleQuickFlickable12viewportSizeEv(
    const QAccessibleQuickFlickable *self) {
  return new QSizeF(self->viewportSize());
}

//  bool QAccessibleQuickFlickable::isIndexed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QAccessibleQuickFlickable9isIndexedEv(
    const QAccessibleQuickFlickable *self) {
  return self->isIndexed();
}

//  void QAccessibleQuickFlickable::setPosition(QPointF position)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleQuickFlickable11setPositionE7QPointF(
    QAccessibleQuickFlickable *self,
    const QPointF *position) {
  self->setPosition(*position);
}

//  QQuickFlickable *QAccessibleQuickFlickable::flickable() const
extern "C" Q_DECL_EXPORT
QQuickFlickable *ritual_ZNK25QAccessibleQuickFlickable9flickableEv(
    const QAccessibleQuickFlickable *self) {
  return self->flickable();
}

//  QAccessibleQuickFlickable as the QAccessibleViewportInterface it is built
//      on
extern "C" Q_DECL_EXPORT
QAccessibleViewportInterface *ritual_cast_QAccessibleQuickFlickable_QAccessibleViewportInterface(
    QAccessibleQuickFlickable *self) {
  return static_cast<QAccessibleViewportInterface *>(self);
}

//  a Python function taken by a CuteQAccessibleQuickFlickable, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleQuickFlickable(
    QAccessibleQuickFlickable *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleQuickFlickable *>(self)->take(key, call);
}

//  QSizeF QAccessibleQuickFlickable::contentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK25QAccessibleQuickFlickable11contentSizeEv(
    const QAccessibleQuickFlickable *self) {
  return new QSizeF(self->QAccessibleQuickFlickable::contentSize());
}

//  QPointF QAccessibleQuickFlickable::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK25QAccessibleQuickFlickable8positionEv(
    const QAccessibleQuickFlickable *self) {
  return new QPointF(self->QAccessibleQuickFlickable::position());
}

//  QSizeF QAccessibleQuickFlickable::viewportSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK25QAccessibleQuickFlickable12viewportSizeEv(
    const QAccessibleQuickFlickable *self) {
  return new QSizeF(self->QAccessibleQuickFlickable::viewportSize());
}

//  bool QAccessibleQuickFlickable::isIndexed() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK25QAccessibleQuickFlickable9isIndexedEv(
    const QAccessibleQuickFlickable *self) {
  return self->QAccessibleQuickFlickable::isIndexed();
}

//  void QAccessibleQuickFlickable::setPosition(QPointF position)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QAccessibleQuickFlickable11setPositionE7QPointF(
    QAccessibleQuickFlickable *self,
    const QPointF *position) {
  self->QAccessibleQuickFlickable::setPosition(*position);
}

#endif  // QT_CONFIG(accessibility)
