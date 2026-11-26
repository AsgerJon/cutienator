//  Written by hand on 2026-11-25 from
//  QtHelp/6.12.0/QtHelp/private/qoptionswidget_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor and 'tr'; 'clear', which calls
//  'setOptions' that the library does not offer; 'validOptions',
//  'selectedOptions', 'setOptions' and the signal
//  'optionSelectionChanged', as they take or give a QStringList;
//  'setNoOptionText' and 'setInvalidOptionText', not inline.
#include <QtHelp/qhelp_global.h>
#include <QtTools/qttools-config.h>
#if QT_CONFIG(fullqthelp)
#include <QtHelp/6.12.0/QtHelp/private/qoptionswidget_p.h>

//  const QMetaObject *QOptionsWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QOptionsWidget10metaObjectEv(
    const QOptionsWidget *self) {
  return self->metaObject();
}

//  QOptionsWidget::~QOptionsWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOptionsWidgetD1Ev(
    QOptionsWidget *self) {
  delete self;
}

#endif  // QT_CONFIG(fullqthelp)
