//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qaccessiblewidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qaccessiblewidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/QtGui>
#include <QtGui/qtestsupport_gui.h>
#include <QtGui/qvulkanfunctions.h>
#include <QtGui/qvulkaninstance.h>
#include <QtGui/qvulkanwindow.h>
#include <QtGui/qcolor.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QAccessibleWidget that Python can take functions over in. Every QAccessibleWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQAccessibleWidgetCall0)(const void *, int *);
typedef void * (*CuteQAccessibleWidgetCall1)(const void *, int *);
typedef int (*CuteQAccessibleWidgetCall2)(const void *, int *);
typedef int (*CuteQAccessibleWidgetCall3)(const void *, const QAccessibleInterface *, int *);
typedef void * (*CuteQAccessibleWidgetCall4)(const void *, int *);
typedef const QRect * (*CuteQAccessibleWidgetCall5)(const void *, int *);
typedef void * (*CuteQAccessibleWidgetCall6)(const void *, int *);
typedef void * (*CuteQAccessibleWidgetCall7)(const void *, int, int *);
typedef QString * (*CuteQAccessibleWidgetCall8)(const void *, int, int *);
typedef int (*CuteQAccessibleWidgetCall9)(const void *, int *);
typedef const QAccessible::State * (*CuteQAccessibleWidgetCall10)(const void *, int *);
typedef const QColor * (*CuteQAccessibleWidgetCall11)(const void *, int *);
typedef const QColor * (*CuteQAccessibleWidgetCall12)(const void *, int *);
typedef void (*CuteQAccessibleWidgetCall13)(const void *, const QString *, int *);
typedef void * (*CuteQAccessibleWidgetCall14)(const void *, int *);
typedef void (*CuteQAccessibleWidgetCall15)(const void *, int, const QString *, int *);
typedef void * (*CuteQAccessibleWidgetCall16)(const void *, int, int, int *);
typedef QString * (*CuteQAccessibleWidgetCall17)(const void *, const QString *, int *);
typedef QString * (*CuteQAccessibleWidgetCall18)(const void *, const QString *, int *);
class CuteQAccessibleWidget : public QAccessibleWidget {
public:
  using QAccessibleWidget::QAccessibleWidget;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[18] = call;
      return true;
    }
    return false;
  }

  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleWidgetCall0 call = reinterpret_cast<CuteQAccessibleWidgetCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }

  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleWidgetCall1 call = reinterpret_cast<CuteQAccessibleWidgetCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }

  //  int QAccessibleWidget::childCount() const
  int childCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleWidgetCall2 call = reinterpret_cast<CuteQAccessibleWidgetCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::childCount();
  }

  //  int QAccessibleWidget::indexOfChild(const QAccessibleInterface
  //      *child) const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleWidgetCall3 call = reinterpret_cast<CuteQAccessibleWidgetCall3>(taken[3]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::indexOfChild(child);
  }

  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleWidgetCall4 call = reinterpret_cast<CuteQAccessibleWidgetCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }

  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleWidgetCall5 call = reinterpret_cast<CuteQAccessibleWidgetCall5>(taken[5]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }

  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleWidgetCall6 call = reinterpret_cast<CuteQAccessibleWidgetCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }

  //  QAccessibleInterface *QAccessibleWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleWidgetCall7 call = reinterpret_cast<CuteQAccessibleWidgetCall7>(taken[7]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }

  //  QString QAccessibleWidget::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleWidgetCall8 call = reinterpret_cast<CuteQAccessibleWidgetCall8>(taken[8]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleWidget::text(t);
  }

  //  QAccessible::Role QAccessibleWidget::role() const
  QAccessible::Role role() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleWidgetCall9 call = reinterpret_cast<CuteQAccessibleWidgetCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }

  //  QAccessible::State QAccessibleWidget::state() const
  QAccessible::State state() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleWidgetCall10 call = reinterpret_cast<CuteQAccessibleWidgetCall10>(taken[10]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::state();
  }

  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleWidgetCall11 call = reinterpret_cast<CuteQAccessibleWidgetCall11>(taken[11]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }

  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleWidgetCall12 call = reinterpret_cast<CuteQAccessibleWidgetCall12>(taken[12]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }

  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleWidgetCall13 call = reinterpret_cast<CuteQAccessibleWidgetCall13>(taken[13]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }

  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleWidgetCall14 call = reinterpret_cast<CuteQAccessibleWidgetCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleObject::object();
  }

  //  void QAccessibleObject::setText(QAccessible::Text t, const QString
  //      &text)
  void setText(QAccessible::Text t, const QString &text) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleWidgetCall15 call = reinterpret_cast<CuteQAccessibleWidgetCall15>(taken[15]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }

  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleWidgetCall16 call = reinterpret_cast<CuteQAccessibleWidgetCall16>(taken[16]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleObject::childAt(x, y);
  }

  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleWidgetCall17 call = reinterpret_cast<CuteQAccessibleWidgetCall17>(taken[17]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionName(name);
  }

  //  QString QAccessibleActionInterface::localizedActionDescription(const
  //      QString &name) const
  QString localizedActionDescription(const QString &name) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleWidgetCall18 call = reinterpret_cast<CuteQAccessibleWidgetCall18>(taken[18]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionDescription(name);
  }
};

//  QAccessibleWidget::QAccessibleWidget(QWidget *o, QAccessible::Role r)
extern "C" Q_DECL_EXPORT
QAccessibleWidget *ritual_ZN17QAccessibleWidgetC1EP7QWidgetN11QAccessible4RoleE(
    QWidget *o,
    QAccessible::Role r) {
  return new CuteQAccessibleWidget(o, r);
}

//  QAccessibleWidget::QAccessibleWidget(QWidget *o, QAccessible::Role r,
//      const QString &name)
extern "C" Q_DECL_EXPORT
QAccessibleWidget *ritual_ZN17QAccessibleWidgetC1EP7QWidgetN11QAccessible4RoleERK7QString(
    QWidget *o,
    QAccessible::Role r,
    const QString *name) {
  return new CuteQAccessibleWidget(o, r, *name);
}

//  bool QAccessibleWidget::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAccessibleWidget7isValidEv(const QAccessibleWidget *self) {
  return self->isValid();
}

//  QWindow *QAccessibleWidget::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK17QAccessibleWidget6windowEv(
    const QAccessibleWidget *self) {
  return self->window();
}

//  int QAccessibleWidget::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAccessibleWidget10childCountEv(
    const QAccessibleWidget *self) {
  return self->childCount();
}

//  int QAccessibleWidget::indexOfChild(const QAccessibleInterface *child)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAccessibleWidget12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleWidget *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

//  QAccessibleInterface *QAccessibleWidget::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK17QAccessibleWidget10focusChildEv(
    const QAccessibleWidget *self) {
  return self->focusChild();
}

//  QRect QAccessibleWidget::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QAccessibleWidget4rectEv(const QAccessibleWidget *self) {
  return new QRect(self->rect());
}

//  QAccessibleInterface *QAccessibleWidget::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK17QAccessibleWidget6parentEv(
    const QAccessibleWidget *self) {
  return self->parent();
}

//  QAccessibleInterface *QAccessibleWidget::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK17QAccessibleWidget5childEi(
    const QAccessibleWidget *self,
    int index) {
  return self->child(index);
}

//  QString QAccessibleWidget::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QAccessibleWidget4textEN11QAccessible4TextE(
    const QAccessibleWidget *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  QAccessible::Role QAccessibleWidget::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK17QAccessibleWidget4roleEv(
    const QAccessibleWidget *self) {
  return self->role();
}

//  QAccessible::State QAccessibleWidget::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK17QAccessibleWidget5stateEv(
    const QAccessibleWidget *self) {
  return new QAccessible::State(self->state());
}

//  QColor QAccessibleWidget::foregroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QAccessibleWidget15foregroundColorEv(
    const QAccessibleWidget *self) {
  return new QColor(self->foregroundColor());
}

//  QColor QAccessibleWidget::backgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QAccessibleWidget15backgroundColorEv(
    const QAccessibleWidget *self) {
  return new QColor(self->backgroundColor());
}

//  QStringList QAccessibleWidget::actionNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QAccessibleWidget11actionNamesEv(
    const QAccessibleWidget *self) {
  return new QList<QString>(self->actionNames());
}

//  void QAccessibleWidget::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAccessibleWidget8doActionERK7QString(
    QAccessibleWidget *self,
    const QString *actionName) {
  self->doAction(*actionName);
}

//  QStringList QAccessibleWidget::keyBindingsForAction(const QString
//      &actionName) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QAccessibleWidget20keyBindingsForActionERK7QString(
    const QAccessibleWidget *self,
    const QString *actionName) {
  return new QList<QString>(self->keyBindingsForAction(*actionName));
}

//  QAccessibleWidget as the QAccessibleActionInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleActionInterface *ritual_cast_QAccessibleWidget_QAccessibleActionInterface(
    QAccessibleWidget *self) {
  return static_cast<QAccessibleActionInterface *>(self);
}

//  a Python function taken by a CuteQAccessibleWidget, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleWidget(
    QAccessibleWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleWidget *>(self)->take(key, call);
}

//  bool QAccessibleWidget::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QAccessibleWidget7isValidEv(
    const QAccessibleWidget *self) {
  return self->QAccessibleWidget::isValid();
}

//  QWindow *QAccessibleWidget::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_own_ZNK17QAccessibleWidget6windowEv(
    const QAccessibleWidget *self) {
  return self->QAccessibleWidget::window();
}

//  int QAccessibleWidget::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QAccessibleWidget10childCountEv(
    const QAccessibleWidget *self) {
  return self->QAccessibleWidget::childCount();
}

//  int QAccessibleWidget::indexOfChild(const QAccessibleInterface *child)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QAccessibleWidget12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleWidget *self,
    const QAccessibleInterface *child) {
  return self->QAccessibleWidget::indexOfChild(child);
}

//  QAccessibleInterface *QAccessibleWidget::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK17QAccessibleWidget10focusChildEv(
    const QAccessibleWidget *self) {
  return self->QAccessibleWidget::focusChild();
}

//  QRect QAccessibleWidget::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK17QAccessibleWidget4rectEv(
    const QAccessibleWidget *self) {
  return new QRect(self->QAccessibleWidget::rect());
}

//  QAccessibleInterface *QAccessibleWidget::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK17QAccessibleWidget6parentEv(
    const QAccessibleWidget *self) {
  return self->QAccessibleWidget::parent();
}

//  QAccessibleInterface *QAccessibleWidget::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK17QAccessibleWidget5childEi(
    const QAccessibleWidget *self,
    int index) {
  return self->QAccessibleWidget::child(index);
}

//  QString QAccessibleWidget::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK17QAccessibleWidget4textEN11QAccessible4TextE(
    const QAccessibleWidget *self,
    QAccessible::Text t) {
  return new QString(self->QAccessibleWidget::text(t));
}

//  QAccessible::Role QAccessibleWidget::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK17QAccessibleWidget4roleEv(
    const QAccessibleWidget *self) {
  return self->QAccessibleWidget::role();
}

//  QAccessible::State QAccessibleWidget::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK17QAccessibleWidget5stateEv(
    const QAccessibleWidget *self) {
  return new QAccessible::State(self->QAccessibleWidget::state());
}

//  QColor QAccessibleWidget::foregroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZNK17QAccessibleWidget15foregroundColorEv(
    const QAccessibleWidget *self) {
  return new QColor(self->QAccessibleWidget::foregroundColor());
}

//  QColor QAccessibleWidget::backgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZNK17QAccessibleWidget15backgroundColorEv(
    const QAccessibleWidget *self) {
  return new QColor(self->QAccessibleWidget::backgroundColor());
}

//  void QAccessibleWidget::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAccessibleWidget8doActionERK7QString(
    QAccessibleWidget *self,
    const QString *actionName) {
  self->QAccessibleWidget::doAction(*actionName);
}
