//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qboxlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qboxlayout.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QVBoxLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QVBoxLayout10metaObjectEv(
    const QVBoxLayout *self) {
  return self->metaObject();
}

//  QString QVBoxLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QVBoxLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVBoxLayout::tr(s, c, n));
}

//  QVBoxLayout::QVBoxLayout()
extern "C" Q_DECL_EXPORT
QVBoxLayout *ritual_ZN11QVBoxLayoutC1Ev() {
  return new QVBoxLayout();
}

//  QVBoxLayout::QVBoxLayout(QWidget *parent)
extern "C" Q_DECL_EXPORT
QVBoxLayout *ritual_ZN11QVBoxLayoutC1EP7QWidget(QWidget *parent) {
  return new QVBoxLayout(parent);
}

//  QVBoxLayout::~QVBoxLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QVBoxLayoutD1Ev(QVBoxLayout *self) {
  delete self;
}
