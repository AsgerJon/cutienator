//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qaccessiblequicklistview_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qaccessiblequicklistview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>
#include <cstring>

//  A QAccessibleQuickListView that Python can take functions over in. Every QAccessibleQuickListView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef const QSizeF * (*CuteQAccessibleQuickListViewCall0)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QPointF * (*CuteQAccessibleQuickListViewCall1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QSizeF * (*CuteQAccessibleQuickListViewCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleQuickListViewCall3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickListViewCall4)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleQuickListViewCall5)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickListViewCall6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleQuickListViewCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickListViewCall8)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickListViewCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickListViewCall10)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickListViewCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickListViewCall12)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleQuickListViewCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickListViewCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickListViewCall15)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickListViewCall16)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickListViewCall17)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickListViewCall18)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickListViewCall19)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickListViewCall20)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickListViewCall21)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickListViewCall22)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickListViewCall23)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickListViewCall24)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickListViewCall25)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickListViewCall26)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickListViewCall27)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickListViewCall28)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickListViewCall29)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickListViewCall30)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleQuickListViewCall31)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickListViewCall32)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickListViewCall33)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickListViewCall34)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickListViewCall35)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickListViewCall36)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleQuickListViewCall37)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleQuickListViewCall38)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickListViewCall39)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickListViewCall40)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleQuickListView : public QAccessibleQuickListView {
public:
  using QAccessibleQuickListView::QAccessibleQuickListView;
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
  //  QSizeF QAccessibleQuickListView::contentSize() const
  QSizeF contentSize() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleQuickListViewCall0 call = reinterpret_cast<CuteQAccessibleQuickListViewCall0>(taken[0]);
      const QSizeF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickListView::contentSize();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QPointF QAccessibleQuickListView::position() const
  QPointF position() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleQuickListViewCall1 call = reinterpret_cast<CuteQAccessibleQuickListViewCall1>(taken[1]);
      const QPointF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickListView::position();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QSizeF QAccessibleQuickListView::viewportSize() const
  QSizeF viewportSize() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleQuickListViewCall2 call = reinterpret_cast<CuteQAccessibleQuickListViewCall2>(taken[2]);
      const QSizeF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickListView::viewportSize();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleQuickListView::isIndexed() const
  bool isIndexed() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleQuickListViewCall3 call = reinterpret_cast<CuteQAccessibleQuickListViewCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickListView::isIndexed();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickListView::setPosition(QPointF position)
  void setPosition(QPointF position) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleQuickListViewCall4 call = reinterpret_cast<CuteQAccessibleQuickListViewCall4>(taken[4]);
      call(this, &position, &handled);
      if (handled) return;
    }
    QAccessibleQuickListView::setPosition(position);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleQuickItem::isValid() const
  bool isValid() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleQuickListViewCall5 call = reinterpret_cast<CuteQAccessibleQuickListViewCall5>(taken[5]);
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
      CuteQAccessibleQuickListViewCall6 call = reinterpret_cast<CuteQAccessibleQuickListViewCall6>(taken[6]);
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
      CuteQAccessibleQuickListViewCall7 call = reinterpret_cast<CuteQAccessibleQuickListViewCall7>(taken[7]);
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
      CuteQAccessibleQuickListViewCall8 call = reinterpret_cast<CuteQAccessibleQuickListViewCall8>(taken[8]);
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
      CuteQAccessibleQuickListViewCall9 call = reinterpret_cast<CuteQAccessibleQuickListViewCall9>(taken[9]);
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
      CuteQAccessibleQuickListViewCall10 call = reinterpret_cast<CuteQAccessibleQuickListViewCall10>(taken[10]);
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
      CuteQAccessibleQuickListViewCall11 call = reinterpret_cast<CuteQAccessibleQuickListViewCall11>(taken[11]);
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
      CuteQAccessibleQuickListViewCall12 call = reinterpret_cast<CuteQAccessibleQuickListViewCall12>(taken[12]);
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
      CuteQAccessibleQuickListViewCall13 call = reinterpret_cast<CuteQAccessibleQuickListViewCall13>(taken[13]);
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
      CuteQAccessibleQuickListViewCall14 call = reinterpret_cast<CuteQAccessibleQuickListViewCall14>(taken[14]);
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
      CuteQAccessibleQuickListViewCall15 call = reinterpret_cast<CuteQAccessibleQuickListViewCall15>(taken[15]);
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
      CuteQAccessibleQuickListViewCall16 call = reinterpret_cast<CuteQAccessibleQuickListViewCall16>(taken[16]);
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
      CuteQAccessibleQuickListViewCall17 call = reinterpret_cast<CuteQAccessibleQuickListViewCall17>(taken[17]);
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
      CuteQAccessibleQuickListViewCall18 call = reinterpret_cast<CuteQAccessibleQuickListViewCall18>(taken[18]);
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
      CuteQAccessibleQuickListViewCall19 call = reinterpret_cast<CuteQAccessibleQuickListViewCall19>(taken[19]);
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
      CuteQAccessibleQuickListViewCall20 call = reinterpret_cast<CuteQAccessibleQuickListViewCall20>(taken[20]);
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
      CuteQAccessibleQuickListViewCall21 call = reinterpret_cast<CuteQAccessibleQuickListViewCall21>(taken[21]);
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
      CuteQAccessibleQuickListViewCall22 call = reinterpret_cast<CuteQAccessibleQuickListViewCall22>(taken[22]);
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
      CuteQAccessibleQuickListViewCall23 call = reinterpret_cast<CuteQAccessibleQuickListViewCall23>(taken[23]);
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
      CuteQAccessibleQuickListViewCall24 call = reinterpret_cast<CuteQAccessibleQuickListViewCall24>(taken[24]);
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
      CuteQAccessibleQuickListViewCall25 call = reinterpret_cast<CuteQAccessibleQuickListViewCall25>(taken[25]);
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
      CuteQAccessibleQuickListViewCall26 call = reinterpret_cast<CuteQAccessibleQuickListViewCall26>(taken[26]);
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
      CuteQAccessibleQuickListViewCall27 call = reinterpret_cast<CuteQAccessibleQuickListViewCall27>(taken[27]);
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
      CuteQAccessibleQuickListViewCall28 call = reinterpret_cast<CuteQAccessibleQuickListViewCall28>(taken[28]);
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
      CuteQAccessibleQuickListViewCall29 call = reinterpret_cast<CuteQAccessibleQuickListViewCall29>(taken[29]);
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
      CuteQAccessibleQuickListViewCall30 call = reinterpret_cast<CuteQAccessibleQuickListViewCall30>(taken[30]);
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
      CuteQAccessibleQuickListViewCall31 call = reinterpret_cast<CuteQAccessibleQuickListViewCall31>(taken[31]);
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
      CuteQAccessibleQuickListViewCall32 call = reinterpret_cast<CuteQAccessibleQuickListViewCall32>(taken[32]);
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
      CuteQAccessibleQuickListViewCall33 call = reinterpret_cast<CuteQAccessibleQuickListViewCall33>(taken[33]);
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
      CuteQAccessibleQuickListViewCall34 call = reinterpret_cast<CuteQAccessibleQuickListViewCall34>(taken[34]);
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
      CuteQAccessibleQuickListViewCall35 call = reinterpret_cast<CuteQAccessibleQuickListViewCall35>(taken[35]);
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
      CuteQAccessibleQuickListViewCall36 call = reinterpret_cast<CuteQAccessibleQuickListViewCall36>(taken[36]);
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
      CuteQAccessibleQuickListViewCall37 call = reinterpret_cast<CuteQAccessibleQuickListViewCall37>(taken[37]);
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
      CuteQAccessibleQuickListViewCall38 call = reinterpret_cast<CuteQAccessibleQuickListViewCall38>(taken[38]);
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
      CuteQAccessibleQuickListViewCall39 call = reinterpret_cast<CuteQAccessibleQuickListViewCall39>(taken[39]);
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
      CuteQAccessibleQuickListViewCall40 call = reinterpret_cast<CuteQAccessibleQuickListViewCall40>(taken[40]);
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

//  QAccessibleQuickListView::QAccessibleQuickListView(QQuickListView
//      *listView)
extern "C" Q_DECL_EXPORT
QAccessibleQuickListView *ritual_ZN24QAccessibleQuickListViewC1EP14QQuickListView(
    QQuickListView *listView) {
  return new CuteQAccessibleQuickListView(listView);
}

//  QSizeF QAccessibleQuickListView::contentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK24QAccessibleQuickListView11contentSizeEv(
    const QAccessibleQuickListView *self) {
  return new QSizeF(self->contentSize());
}

//  QPointF QAccessibleQuickListView::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QAccessibleQuickListView8positionEv(
    const QAccessibleQuickListView *self) {
  return new QPointF(self->position());
}

//  QSizeF QAccessibleQuickListView::viewportSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK24QAccessibleQuickListView12viewportSizeEv(
    const QAccessibleQuickListView *self) {
  return new QSizeF(self->viewportSize());
}

//  bool QAccessibleQuickListView::isIndexed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAccessibleQuickListView9isIndexedEv(
    const QAccessibleQuickListView *self) {
  return self->isIndexed();
}

//  void QAccessibleQuickListView::setPosition(QPointF position)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleQuickListView11setPositionE7QPointF(
    QAccessibleQuickListView *self,
    const QPointF *position) {
  self->setPosition(*position);
}

//  QQuickListView *QAccessibleQuickListView::listView() const
extern "C" Q_DECL_EXPORT
QQuickListView *ritual_ZNK24QAccessibleQuickListView8listViewEv(
    const QAccessibleQuickListView *self) {
  return self->listView();
}

//  QAccessibleQuickListView as the QAccessibleViewportInterface it is built
//      on
extern "C" Q_DECL_EXPORT
QAccessibleViewportInterface *ritual_cast_QAccessibleQuickListView_QAccessibleViewportInterface(
    QAccessibleQuickListView *self) {
  return static_cast<QAccessibleViewportInterface *>(self);
}

//  a Python function taken by a CuteQAccessibleQuickListView, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleQuickListView(
    QAccessibleQuickListView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleQuickListView *>(self)->take(key, call);
}

//  QSizeF QAccessibleQuickListView::contentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK24QAccessibleQuickListView11contentSizeEv(
    const QAccessibleQuickListView *self) {
  return new QSizeF(self->QAccessibleQuickListView::contentSize());
}

//  QPointF QAccessibleQuickListView::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK24QAccessibleQuickListView8positionEv(
    const QAccessibleQuickListView *self) {
  return new QPointF(self->QAccessibleQuickListView::position());
}

//  QSizeF QAccessibleQuickListView::viewportSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK24QAccessibleQuickListView12viewportSizeEv(
    const QAccessibleQuickListView *self) {
  return new QSizeF(self->QAccessibleQuickListView::viewportSize());
}

//  bool QAccessibleQuickListView::isIndexed() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QAccessibleQuickListView9isIndexedEv(
    const QAccessibleQuickListView *self) {
  return self->QAccessibleQuickListView::isIndexed();
}

//  void QAccessibleQuickListView::setPosition(QPointF position)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAccessibleQuickListView11setPositionE7QPointF(
    QAccessibleQuickListView *self,
    const QPointF *position) {
  self->QAccessibleQuickListView::setPosition(*position);
}

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
