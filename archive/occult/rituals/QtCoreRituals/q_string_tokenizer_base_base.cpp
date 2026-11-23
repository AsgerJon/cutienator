//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringtokenizer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qstringtokenizer.h>

//  QStringTokenizerBaseBase::~QStringTokenizerBaseBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QStringTokenizerBaseBaseD1Ev(
    QStringTokenizerBaseBase *self) {
  delete self;
}

//  QStringTokenizerBaseBase::QStringTokenizerBaseBase(Qt::SplitBehavior sb,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
QStringTokenizerBaseBase *ritual_ZN24QStringTokenizerBaseBaseC1E6QFlagsIN2Qt18SplitBehaviorFlagsEENS1_15CaseSensitivityE(
    int sb,
    Qt::CaseSensitivity cs) {
  return new QStringTokenizerBaseBase(
      QFlags<Qt::SplitBehaviorFlags>::fromInt(sb),
      cs);
}
