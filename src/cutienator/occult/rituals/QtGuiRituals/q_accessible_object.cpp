//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessibleobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessibleobject.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtGui/qaccessible.h>
#include <QtGui/qcolor.h>
#include <cstring>

//  A QAccessibleObject that Python can take functions over in. Every QAccessibleObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleObjectCall0)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleObjectCall1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleObjectCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleObjectCall3)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleObjectCall4)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleObjectCall5)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleObjectCall6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleObjectCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleObjectCall8)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleObjectCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleObjectCall10)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleObjectCall11)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleObjectCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleObjectCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleObjectCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleObjectCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleObject : public QAccessibleObject {
public:
  using QAccessibleObject::QAccessibleObject;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
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
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
  //  bool QAccessibleObject::isValid() const
  bool isValid() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleObjectCall0 call = reinterpret_cast<CuteQAccessibleObjectCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleObject::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleObjectCall1 call = reinterpret_cast<CuteQAccessibleObjectCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleObject::object();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleObject::rect() const
  QRect rect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleObjectCall2 call = reinterpret_cast<CuteQAccessibleObjectCall2>(taken[2]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleObject::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleObject::setText(QAccessible::Text t, const QString
  //      &text)
  void setText(QAccessible::Text t, const QString &text) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleObjectCall3 call = reinterpret_cast<CuteQAccessibleObjectCall3>(taken[3]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleObjectCall4 call = reinterpret_cast<CuteQAccessibleObjectCall4>(taken[4]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleObject::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleInterface::window() const
  QWindow *window() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleObjectCall5 call = reinterpret_cast<CuteQAccessibleObjectCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleInterface::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleInterface::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleObjectCall6 call = reinterpret_cast<CuteQAccessibleObjectCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleInterface::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleInterface::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleObjectCall7 call = reinterpret_cast<CuteQAccessibleObjectCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleInterface::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleObjectCall8 call = reinterpret_cast<CuteQAccessibleObjectCall8>(taken[8]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleInterface::childCount() const
  int childCount() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleObjectCall9 call = reinterpret_cast<CuteQAccessibleObjectCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleInterface::indexOfChild(const QAccessibleInterface
  //      *a0) const
  int indexOfChild(const QAccessibleInterface *a0) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleObjectCall10 call = reinterpret_cast<CuteQAccessibleObjectCall10>(taken[10]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleInterface::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleObjectCall11 call = reinterpret_cast<CuteQAccessibleObjectCall11>(taken[11]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleInterface::role() const
  QAccessible::Role role() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleObjectCall12 call = reinterpret_cast<CuteQAccessibleObjectCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleInterface::state() const
  QAccessible::State state() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleObjectCall13 call = reinterpret_cast<CuteQAccessibleObjectCall13>(taken[13]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleInterface::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleObjectCall14 call = reinterpret_cast<CuteQAccessibleObjectCall14>(taken[14]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleInterface::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleInterface::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleObjectCall15 call = reinterpret_cast<CuteQAccessibleObjectCall15>(taken[15]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleInterface::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)
};

//  bool QAccessibleObject::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAccessibleObject7isValidEv(const QAccessibleObject *self) {
  return self->isValid();
}

//  QObject *QAccessibleObject::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK17QAccessibleObject6objectEv(
    const QAccessibleObject *self) {
  return self->object();
}

//  QRect QAccessibleObject::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QAccessibleObject4rectEv(const QAccessibleObject *self) {
  return new QRect(self->rect());
}

//  void QAccessibleObject::setText(QAccessible::Text t, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAccessibleObject7setTextEN11QAccessible4TextERK7QString(
    QAccessibleObject *self,
    QAccessible::Text t,
    const QString *text) {
  self->setText(t, *text);
}

//  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK17QAccessibleObject7childAtEii(
    const QAccessibleObject *self,
    int x,
    int y) {
  return self->childAt(x, y);
}

//  QAccessibleObject::~QAccessibleObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAccessibleObjectD1Ev(QAccessibleObject *self) {
  delete self;
}

//  a Python function taken by a CuteQAccessibleObject, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleObject(
    QAccessibleObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleObject *>(self)->take(key, call);
}

//  bool QAccessibleObject::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QAccessibleObject7isValidEv(
    const QAccessibleObject *self) {
  return self->QAccessibleObject::isValid();
}

//  QObject *QAccessibleObject::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK17QAccessibleObject6objectEv(
    const QAccessibleObject *self) {
  return self->QAccessibleObject::object();
}

//  QRect QAccessibleObject::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK17QAccessibleObject4rectEv(
    const QAccessibleObject *self) {
  return new QRect(self->QAccessibleObject::rect());
}

//  void QAccessibleObject::setText(QAccessible::Text t, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAccessibleObject7setTextEN11QAccessible4TextERK7QString(
    QAccessibleObject *self,
    QAccessible::Text t,
    const QString *text) {
  self->QAccessibleObject::setText(t, *text);
}

//  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK17QAccessibleObject7childAtEii(
    const QAccessibleObject *self,
    int x,
    int y) {
  return self->QAccessibleObject::childAt(x, y);
}

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
