//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QAccessibleInterface that Python can take functions over in. Every QAccessibleInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleInterfaceCall0)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleInterfaceCall1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleInterfaceCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleInterfaceCall3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleInterfaceCall4)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleInterfaceCall5)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleInterfaceCall6)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleInterfaceCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleInterfaceCall8)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleInterfaceCall9)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleInterfaceCall10)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleInterfaceCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleInterfaceCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleInterfaceCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleInterfaceCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleInterfaceCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleInterface : public QAccessibleInterface {
public:
  using QAccessibleInterface::QAccessibleInterface;
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
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
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
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
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
  //  bool QAccessibleInterface::isValid() const
  bool isValid() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleInterfaceCall0 call = reinterpret_cast<CuteQAccessibleInterfaceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleInterface::object() const
  QObject *object() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleInterfaceCall1 call = reinterpret_cast<CuteQAccessibleInterfaceCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleInterface::window() const
  QWindow *window() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleInterfaceCall2 call = reinterpret_cast<CuteQAccessibleInterfaceCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleInterface::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleInterface::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleInterfaceCall3 call = reinterpret_cast<CuteQAccessibleInterfaceCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleInterface::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleInterface::childAt(int x, int y)
  //      const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleInterfaceCall4 call = reinterpret_cast<CuteQAccessibleInterfaceCall4>(taken[4]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleInterface::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleInterfaceCall5 call = reinterpret_cast<CuteQAccessibleInterfaceCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleInterface::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleInterfaceCall6 call = reinterpret_cast<CuteQAccessibleInterfaceCall6>(taken[6]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleInterface::childCount() const
  int childCount() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleInterfaceCall7 call = reinterpret_cast<CuteQAccessibleInterfaceCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleInterfaceCall8 call = reinterpret_cast<CuteQAccessibleInterfaceCall8>(taken[8]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleInterface::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleInterfaceCall9 call = reinterpret_cast<CuteQAccessibleInterfaceCall9>(taken[9]);
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
  //  void QAccessibleInterface::setText(QAccessible::Text t, const QString
  //      &text)
  void setText(QAccessible::Text t, const QString &text) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleInterfaceCall10 call = reinterpret_cast<CuteQAccessibleInterfaceCall10>(taken[10]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleInterface::rect() const
  QRect rect() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleInterfaceCall11 call = reinterpret_cast<CuteQAccessibleInterfaceCall11>(taken[11]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleInterface::role() const
  QAccessible::Role role() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleInterfaceCall12 call = reinterpret_cast<CuteQAccessibleInterfaceCall12>(taken[12]);
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
      CuteQAccessibleInterfaceCall13 call = reinterpret_cast<CuteQAccessibleInterfaceCall13>(taken[13]);
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
      CuteQAccessibleInterfaceCall14 call = reinterpret_cast<CuteQAccessibleInterfaceCall14>(taken[14]);
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
      CuteQAccessibleInterfaceCall15 call = reinterpret_cast<CuteQAccessibleInterfaceCall15>(taken[15]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleInterface::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)
};

//  QAccessibleInterface::~QAccessibleInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAccessibleInterfaceD1Ev(QAccessibleInterface *self) {
  delete self;
}

//  bool QAccessibleInterface::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAccessibleInterface7isValidEv(
    const QAccessibleInterface *self) {
  return self->isValid();
}

//  QObject *QAccessibleInterface::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK20QAccessibleInterface6objectEv(
    const QAccessibleInterface *self) {
  return self->object();
}

//  QWindow *QAccessibleInterface::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK20QAccessibleInterface6windowEv(
    const QAccessibleInterface *self) {
  return self->window();
}

//  QAccessibleInterface *QAccessibleInterface::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleInterface10focusChildEv(
    const QAccessibleInterface *self) {
  return self->focusChild();
}

//  QAccessibleInterface *QAccessibleInterface::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleInterface7childAtEii(
    const QAccessibleInterface *self,
    int x,
    int y) {
  return self->childAt(x, y);
}

//  QAccessibleInterface *QAccessibleInterface::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleInterface6parentEv(
    const QAccessibleInterface *self) {
  return self->parent();
}

//  QAccessibleInterface *QAccessibleInterface::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleInterface5childEi(
    const QAccessibleInterface *self,
    int index) {
  return self->child(index);
}

//  int QAccessibleInterface::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleInterface10childCountEv(
    const QAccessibleInterface *self) {
  return self->childCount();
}

//  int QAccessibleInterface::indexOfChild(const QAccessibleInterface *a0)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleInterface12indexOfChildEPKS_(
    const QAccessibleInterface *self,
    const QAccessibleInterface *a0) {
  return self->indexOfChild(a0);
}

//  QString QAccessibleInterface::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QAccessibleInterface4textEN11QAccessible4TextE(
    const QAccessibleInterface *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  void QAccessibleInterface::setText(QAccessible::Text t, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString(
    QAccessibleInterface *self,
    QAccessible::Text t,
    const QString *text) {
  self->setText(t, *text);
}

//  QRect QAccessibleInterface::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK20QAccessibleInterface4rectEv(
    const QAccessibleInterface *self) {
  return new QRect(self->rect());
}

//  QAccessible::Role QAccessibleInterface::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK20QAccessibleInterface4roleEv(
    const QAccessibleInterface *self) {
  return self->role();
}

//  QAccessible::State QAccessibleInterface::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK20QAccessibleInterface5stateEv(
    const QAccessibleInterface *self) {
  return new QAccessible::State(self->state());
}

//  QColor QAccessibleInterface::foregroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QAccessibleInterface15foregroundColorEv(
    const QAccessibleInterface *self) {
  return new QColor(self->foregroundColor());
}

//  QColor QAccessibleInterface::backgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QAccessibleInterface15backgroundColorEv(
    const QAccessibleInterface *self) {
  return new QColor(self->backgroundColor());
}

//  QAccessibleTextInterface *QAccessibleInterface::textInterface()
extern "C" Q_DECL_EXPORT
QAccessibleTextInterface *ritual_ZN20QAccessibleInterface13textInterfaceEv(
    QAccessibleInterface *self) {
  return self->textInterface();
}

//  QAccessibleEditableTextInterface
//      *QAccessibleInterface::editableTextInterface()
extern "C" Q_DECL_EXPORT
QAccessibleEditableTextInterface *ritual_ZN20QAccessibleInterface21editableTextInterfaceEv(
    QAccessibleInterface *self) {
  return self->editableTextInterface();
}

//  QAccessibleValueInterface *QAccessibleInterface::valueInterface()
extern "C" Q_DECL_EXPORT
QAccessibleValueInterface *ritual_ZN20QAccessibleInterface14valueInterfaceEv(
    QAccessibleInterface *self) {
  return self->valueInterface();
}

//  QAccessibleActionInterface *QAccessibleInterface::actionInterface()
extern "C" Q_DECL_EXPORT
QAccessibleActionInterface *ritual_ZN20QAccessibleInterface15actionInterfaceEv(
    QAccessibleInterface *self) {
  return self->actionInterface();
}

//  QAccessibleImageInterface *QAccessibleInterface::imageInterface()
extern "C" Q_DECL_EXPORT
QAccessibleImageInterface *ritual_ZN20QAccessibleInterface14imageInterfaceEv(
    QAccessibleInterface *self) {
  return self->imageInterface();
}

//  QAccessibleTableInterface *QAccessibleInterface::tableInterface()
extern "C" Q_DECL_EXPORT
QAccessibleTableInterface *ritual_ZN20QAccessibleInterface14tableInterfaceEv(
    QAccessibleInterface *self) {
  return self->tableInterface();
}

//  QAccessibleTableCellInterface *QAccessibleInterface::tableCellInterface()
extern "C" Q_DECL_EXPORT
QAccessibleTableCellInterface *ritual_ZN20QAccessibleInterface18tableCellInterfaceEv(
    QAccessibleInterface *self) {
  return self->tableCellInterface();
}

//  QAccessibleHyperlinkInterface *QAccessibleInterface::hyperlinkInterface()
extern "C" Q_DECL_EXPORT
QAccessibleHyperlinkInterface *ritual_ZN20QAccessibleInterface18hyperlinkInterfaceEv(
    QAccessibleInterface *self) {
  return self->hyperlinkInterface();
}

//  QAccessibleSelectionInterface *QAccessibleInterface::selectionInterface()
extern "C" Q_DECL_EXPORT
QAccessibleSelectionInterface *ritual_ZN20QAccessibleInterface18selectionInterfaceEv(
    QAccessibleInterface *self) {
  return self->selectionInterface();
}

//  QAccessibleAttributesInterface
//      *QAccessibleInterface::attributesInterface()
extern "C" Q_DECL_EXPORT
QAccessibleAttributesInterface *ritual_ZN20QAccessibleInterface19attributesInterfaceEv(
    QAccessibleInterface *self) {
  return self->attributesInterface();
}

//  QAccessibleViewportInterface *QAccessibleInterface::viewportInterface()
extern "C" Q_DECL_EXPORT
QAccessibleViewportInterface *ritual_ZN20QAccessibleInterface17viewportInterfaceEv(
    QAccessibleInterface *self) {
  return self->viewportInterface();
}

//  a Python function taken by a CuteQAccessibleInterface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleInterface(
    QAccessibleInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleInterface *>(self)->take(key, call);
}

//  QWindow *QAccessibleInterface::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_own_ZNK20QAccessibleInterface6windowEv(
    const QAccessibleInterface *self) {
  return self->QAccessibleInterface::window();
}

//  QAccessibleInterface *QAccessibleInterface::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK20QAccessibleInterface10focusChildEv(
    const QAccessibleInterface *self) {
  return self->QAccessibleInterface::focusChild();
}

//  QColor QAccessibleInterface::foregroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZNK20QAccessibleInterface15foregroundColorEv(
    const QAccessibleInterface *self) {
  return new QColor(self->QAccessibleInterface::foregroundColor());
}

//  QColor QAccessibleInterface::backgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZNK20QAccessibleInterface15backgroundColorEv(
    const QAccessibleInterface *self) {
  return new QColor(self->QAccessibleInterface::backgroundColor());
}

//  QList<QAccessibleInterface *>::QList()
extern "C" Q_DECL_EXPORT
QList<QAccessibleInterface *> *ritual_list_make_QAccessibleInterface_ptr() {
  return new QList<QAccessibleInterface *>();
}

//  void QList<QAccessibleInterface *>::append(const QAccessibleInterface *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QAccessibleInterface_ptr(
    QList<QAccessibleInterface *> *self,
    QAccessibleInterface *element) {
  self->append(element);
}

//  qsizetype QList<QAccessibleInterface *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QAccessibleInterface_ptr(
    const QList<QAccessibleInterface *> *self) {
  return self->size();
}

//  const QAccessibleInterface * &QList<QAccessibleInterface *>::at(qsizetype
//      i) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_list_at_QAccessibleInterface_ptr(
    const QList<QAccessibleInterface *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QAccessibleInterface *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QAccessibleInterface_ptr(
    QList<QAccessibleInterface *> *self) {
  delete self;
}

#endif  // QT_CONFIG(accessibility)
