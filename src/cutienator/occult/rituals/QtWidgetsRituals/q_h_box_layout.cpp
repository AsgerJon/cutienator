//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qboxlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qboxlayout.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QHBoxLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QHBoxLayout10metaObjectEv(
    const QHBoxLayout *self) {
  return self->metaObject();
}

//  QString QHBoxLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QHBoxLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHBoxLayout::tr(s, c, n));
}

//  QHBoxLayout::QHBoxLayout()
extern "C" Q_DECL_EXPORT
QHBoxLayout *ritual_ZN11QHBoxLayoutC1Ev() {
  return new QHBoxLayout();
}

//  QHBoxLayout::QHBoxLayout(QWidget *parent)
extern "C" Q_DECL_EXPORT
QHBoxLayout *ritual_ZN11QHBoxLayoutC1EP7QWidget(QWidget *parent) {
  return new QHBoxLayout(parent);
}

//  QHBoxLayout::~QHBoxLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHBoxLayoutD1Ev(QHBoxLayout *self) {
  delete self;
}
