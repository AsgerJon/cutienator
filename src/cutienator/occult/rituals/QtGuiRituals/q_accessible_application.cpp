//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessibleobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessibleobject.h>
#include <QtCore/qstring.h>
#include <QtGui/QtGui>
#include <QtGui/qtestsupport_gui.h>
#include <QtGui/qvulkanfunctions.h>
#include <QtGui/qvulkaninstance.h>
#include <QtGui/qvulkanwindow.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <cstring>

//  A QAccessibleApplication that Python can take functions over in. Every QAccessibleApplication
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAccessibleApplicationCall0)(const void *, int *);
typedef int (*CuteQAccessibleApplicationCall1)(const void *, int *);
typedef int (*CuteQAccessibleApplicationCall2)(const void *, const QAccessibleInterface *, int *);
typedef void * (*CuteQAccessibleApplicationCall3)(const void *, int *);
typedef void * (*CuteQAccessibleApplicationCall4)(const void *, int *);
typedef void * (*CuteQAccessibleApplicationCall5)(const void *, int, int *);
typedef int (*CuteQAccessibleApplicationCall6)(const void *, int *);
typedef const QAccessible::State * (*CuteQAccessibleApplicationCall7)(const void *, int *);
typedef bool (*CuteQAccessibleApplicationCall8)(const void *, int *);
typedef void * (*CuteQAccessibleApplicationCall9)(const void *, int *);
typedef const QRect * (*CuteQAccessibleApplicationCall10)(const void *, int *);
typedef void * (*CuteQAccessibleApplicationCall11)(const void *, int, int, int *);
typedef const QColor * (*CuteQAccessibleApplicationCall12)(const void *, int *);
typedef const QColor * (*CuteQAccessibleApplicationCall13)(const void *, int *);
class CuteQAccessibleApplication : public QAccessibleApplication {
public:
  using QAccessibleApplication::QAccessibleApplication;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[13] = call;
      return true;
    }
    return false;
  }

  //  QWindow *QAccessibleApplication::window() const
  QWindow *window() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleApplicationCall0 call = reinterpret_cast<CuteQAccessibleApplicationCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleApplication::window();
  }

  //  int QAccessibleApplication::childCount() const
  int childCount() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleApplicationCall1 call = reinterpret_cast<CuteQAccessibleApplicationCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleApplication::childCount();
  }

  //  int QAccessibleApplication::indexOfChild(const QAccessibleInterface
  //      *a0) const
  int indexOfChild(const QAccessibleInterface *a0) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleApplicationCall2 call = reinterpret_cast<CuteQAccessibleApplicationCall2>(taken[2]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAccessibleApplication::indexOfChild(a0);
  }

  //  QAccessibleInterface *QAccessibleApplication::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleApplicationCall3 call = reinterpret_cast<CuteQAccessibleApplicationCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleApplication::focusChild();
  }

  //  QAccessibleInterface *QAccessibleApplication::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleApplicationCall4 call = reinterpret_cast<CuteQAccessibleApplicationCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleApplication::parent();
  }

  //  QAccessibleInterface *QAccessibleApplication::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleApplicationCall5 call = reinterpret_cast<CuteQAccessibleApplicationCall5>(taken[5]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleApplication::child(index);
  }

  //  QAccessible::Role QAccessibleApplication::role() const
  QAccessible::Role role() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleApplicationCall6 call = reinterpret_cast<CuteQAccessibleApplicationCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleApplication::role();
  }

  //  QAccessible::State QAccessibleApplication::state() const
  QAccessible::State state() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleApplicationCall7 call = reinterpret_cast<CuteQAccessibleApplicationCall7>(taken[7]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleApplication::state();
  }

  //  bool QAccessibleObject::isValid() const
  bool isValid() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleApplicationCall8 call = reinterpret_cast<CuteQAccessibleApplicationCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleObject::isValid();
  }

  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleApplicationCall9 call = reinterpret_cast<CuteQAccessibleApplicationCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleObject::object();
  }

  //  QRect QAccessibleObject::rect() const
  QRect rect() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleApplicationCall10 call = reinterpret_cast<CuteQAccessibleApplicationCall10>(taken[10]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleObject::rect();
  }

  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleApplicationCall11 call = reinterpret_cast<CuteQAccessibleApplicationCall11>(taken[11]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleObject::childAt(x, y);
  }

  //  QColor QAccessibleInterface::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleApplicationCall12 call = reinterpret_cast<CuteQAccessibleApplicationCall12>(taken[12]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleInterface::foregroundColor();
  }

  //  QColor QAccessibleInterface::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleApplicationCall13 call = reinterpret_cast<CuteQAccessibleApplicationCall13>(taken[13]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleInterface::backgroundColor();
  }
};

//  QAccessibleApplication::QAccessibleApplication()
extern "C" Q_DECL_EXPORT
QAccessibleApplication *ritual_ZN22QAccessibleApplicationC1Ev() {
  return new CuteQAccessibleApplication();
}

//  QWindow *QAccessibleApplication::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK22QAccessibleApplication6windowEv(
    const QAccessibleApplication *self) {
  return self->window();
}

//  int QAccessibleApplication::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QAccessibleApplication10childCountEv(
    const QAccessibleApplication *self) {
  return self->childCount();
}

//  int QAccessibleApplication::indexOfChild(const QAccessibleInterface *a0)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QAccessibleApplication12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleApplication *self,
    const QAccessibleInterface *a0) {
  return self->indexOfChild(a0);
}

//  QAccessibleInterface *QAccessibleApplication::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK22QAccessibleApplication10focusChildEv(
    const QAccessibleApplication *self) {
  return self->focusChild();
}

//  QAccessibleInterface *QAccessibleApplication::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK22QAccessibleApplication6parentEv(
    const QAccessibleApplication *self) {
  return self->parent();
}

//  QAccessibleInterface *QAccessibleApplication::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK22QAccessibleApplication5childEi(
    const QAccessibleApplication *self,
    int index) {
  return self->child(index);
}

//  QString QAccessibleApplication::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QAccessibleApplication4textEN11QAccessible4TextE(
    const QAccessibleApplication *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  QAccessible::Role QAccessibleApplication::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK22QAccessibleApplication4roleEv(
    const QAccessibleApplication *self) {
  return self->role();
}

//  QAccessible::State QAccessibleApplication::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK22QAccessibleApplication5stateEv(
    const QAccessibleApplication *self) {
  return new QAccessible::State(self->state());
}

//  a Python function taken by a CuteQAccessibleApplication, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleApplication(
    QAccessibleApplication *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleApplication *>(self)->take(key, call);
}

//  QWindow *QAccessibleApplication::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_own_ZNK22QAccessibleApplication6windowEv(
    const QAccessibleApplication *self) {
  return self->QAccessibleApplication::window();
}

//  int QAccessibleApplication::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QAccessibleApplication10childCountEv(
    const QAccessibleApplication *self) {
  return self->QAccessibleApplication::childCount();
}

//  int QAccessibleApplication::indexOfChild(const QAccessibleInterface *a0)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QAccessibleApplication12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleApplication *self,
    const QAccessibleInterface *a0) {
  return self->QAccessibleApplication::indexOfChild(a0);
}

//  QAccessibleInterface *QAccessibleApplication::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK22QAccessibleApplication10focusChildEv(
    const QAccessibleApplication *self) {
  return self->QAccessibleApplication::focusChild();
}

//  QAccessibleInterface *QAccessibleApplication::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK22QAccessibleApplication6parentEv(
    const QAccessibleApplication *self) {
  return self->QAccessibleApplication::parent();
}

//  QAccessibleInterface *QAccessibleApplication::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK22QAccessibleApplication5childEi(
    const QAccessibleApplication *self,
    int index) {
  return self->QAccessibleApplication::child(index);
}

//  QAccessible::Role QAccessibleApplication::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK22QAccessibleApplication4roleEv(
    const QAccessibleApplication *self) {
  return self->QAccessibleApplication::role();
}

//  QAccessible::State QAccessibleApplication::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK22QAccessibleApplication5stateEv(
    const QAccessibleApplication *self) {
  return new QAccessible::State(self->QAccessibleApplication::state());
}
