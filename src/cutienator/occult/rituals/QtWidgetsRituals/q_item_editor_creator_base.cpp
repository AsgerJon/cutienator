//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qitemeditorfactory.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#include <QtWidgets/qitemeditorfactory.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QItemEditorCreatorBase that Python can take functions over in. Every QItemEditorCreatorBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
typedef void * (*CuteQItemEditorCreatorBaseCall0)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QByteArray * (*CuteQItemEditorCreatorBaseCall1)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
class CuteQItemEditorCreatorBase : public QItemEditorCreatorBase {
public:
  using QItemEditorCreatorBase::QItemEditorCreatorBase;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK22QItemEditorCreatorBase12createWidgetEP7QWidget")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK22QItemEditorCreatorBase17valuePropertyNameEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
    return false;
  }

#if QT_CONFIG(itemviews)
  //  QWidget *QItemEditorCreatorBase::createWidget(QWidget *parent) const
  QWidget *createWidget(QWidget *parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQItemEditorCreatorBaseCall0 call = reinterpret_cast<CuteQItemEditorCreatorBaseCall0>(taken[0]);
      void * given = call(this, parent, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QByteArray QItemEditorCreatorBase::valuePropertyName() const
  QByteArray valuePropertyName() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQItemEditorCreatorBaseCall1 call = reinterpret_cast<CuteQItemEditorCreatorBaseCall1>(taken[1]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemviews)
};

//  QItemEditorCreatorBase::~QItemEditorCreatorBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemEditorCreatorBaseD1Ev(QItemEditorCreatorBase *self) {
  delete self;
}

//  QWidget *QItemEditorCreatorBase::createWidget(QWidget *parent) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK22QItemEditorCreatorBase12createWidgetEP7QWidget(
    const QItemEditorCreatorBase *self,
    QWidget *parent) {
  return self->createWidget(parent);
}

//  QByteArray QItemEditorCreatorBase::valuePropertyName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK22QItemEditorCreatorBase17valuePropertyNameEv(
    const QItemEditorCreatorBase *self) {
  return new QByteArray(self->valuePropertyName());
}

//  a Python function taken by a CuteQItemEditorCreatorBase, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QItemEditorCreatorBase(
    QItemEditorCreatorBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQItemEditorCreatorBase *>(self)->take(key, call);
}

#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(itemviews)
