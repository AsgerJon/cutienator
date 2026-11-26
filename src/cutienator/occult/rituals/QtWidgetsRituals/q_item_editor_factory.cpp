//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qitemeditorfactory.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#include <QtWidgets/qitemeditorfactory.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QItemEditorFactory that Python can take functions over in. Every QItemEditorFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
typedef void * (*CuteQItemEditorFactoryCall0)(const void *, int, QWidget *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QByteArray * (*CuteQItemEditorFactoryCall1)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
class CuteQItemEditorFactory : public QItemEditorFactory {
public:
  using QItemEditorFactory::QItemEditorFactory;
  CuteQItemEditorFactory(const QItemEditorFactory & other) : QItemEditorFactory(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK18QItemEditorFactory12createEditorEiP7QWidget")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK18QItemEditorFactory17valuePropertyNameEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
    return false;
  }

#if QT_CONFIG(itemviews)
  //  QWidget *QItemEditorFactory::createEditor(int userType, QWidget
  //      *parent) const
  QWidget *createEditor(int userType, QWidget *parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQItemEditorFactoryCall0 call = reinterpret_cast<CuteQItemEditorFactoryCall0>(taken[0]);
      void * given = call(this, userType, parent, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QItemEditorFactory::createEditor(userType, parent);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QByteArray QItemEditorFactory::valuePropertyName(int userType) const
  QByteArray valuePropertyName(int userType) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQItemEditorFactoryCall1 call = reinterpret_cast<CuteQItemEditorFactoryCall1>(taken[1]);
      const QByteArray * given = call(this, userType, &handled);
      if (handled && given) return *given;
    }
    return QItemEditorFactory::valuePropertyName(userType);
  }
#endif  // QT_CONFIG(itemviews)
};

//  QItemEditorFactory::QItemEditorFactory()
extern "C" Q_DECL_EXPORT
QItemEditorFactory *ritual_ZN18QItemEditorFactoryC1Ev() {
  return new CuteQItemEditorFactory();
}

//  QItemEditorFactory::~QItemEditorFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QItemEditorFactoryD1Ev(QItemEditorFactory *self) {
  delete self;
}

//  QWidget *QItemEditorFactory::createEditor(int userType, QWidget *parent)
//      const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK18QItemEditorFactory12createEditorEiP7QWidget(
    const QItemEditorFactory *self,
    int userType,
    QWidget *parent) {
  return self->createEditor(userType, parent);
}

//  QByteArray QItemEditorFactory::valuePropertyName(int userType) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QItemEditorFactory17valuePropertyNameEi(
    const QItemEditorFactory *self,
    int userType) {
  return new QByteArray(self->valuePropertyName(userType));
}

//  void QItemEditorFactory::registerEditor(int userType,
//      QItemEditorCreatorBase *creator)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QItemEditorFactory14registerEditorEiP22QItemEditorCreatorBase(
    QItemEditorFactory *self,
    int userType,
    QItemEditorCreatorBase *creator) {
  self->registerEditor(userType, creator);
}

//  const QItemEditorFactory *QItemEditorFactory::defaultFactory()
extern "C" Q_DECL_EXPORT
const QItemEditorFactory *ritual_ZN18QItemEditorFactory14defaultFactoryEv() {
  return QItemEditorFactory::defaultFactory();
}

//  void QItemEditorFactory::setDefaultFactory(QItemEditorFactory *factory)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QItemEditorFactory17setDefaultFactoryEPS_(
    QItemEditorFactory *factory) {
  QItemEditorFactory::setDefaultFactory(factory);
}

//  a Python function taken by a CuteQItemEditorFactory, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QItemEditorFactory(
    QItemEditorFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQItemEditorFactory *>(self)->take(key, call);
}

//  QWidget *QItemEditorFactory::createEditor(int userType, QWidget *parent)
//      const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK18QItemEditorFactory12createEditorEiP7QWidget(
    const QItemEditorFactory *self,
    int userType,
    QWidget *parent) {
  return self->QItemEditorFactory::createEditor(userType, parent);
}

//  QByteArray QItemEditorFactory::valuePropertyName(int userType) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK18QItemEditorFactory17valuePropertyNameEi(
    const QItemEditorFactory *self,
    int userType) {
  return new QByteArray(
      self->QItemEditorFactory::valuePropertyName(
          userType));
}

#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(itemviews)
